from typing import List, Optional
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, \
    HumanMessagePromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
import os
from dotenv import load_dotenv


class RAGAgent:
    def __init__(
            self,
            model_name: str = "gemini-2.0-flash-exp",
            embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
            chunk_size: int = 1000,
            chunk_overlap: int = 200
    ):
        """
        Initialize the RAG Agent with specified models and parameters.

        Args:
            model_name: The name of the Gemini model to use
            embedding_model: The name of the embedding model to use
            chunk_size: Size of text chunks for splitting documents
            chunk_overlap: Overlap between text chunks
        """
        load_dotenv()

        # Configure Gemini
        GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")  # Changed to use GEMINI_API_KEY
        if not GOOGLE_API_KEY:
            raise ValueError("GEMINI_API_KEY not found in environment variables")

        genai.configure(api_key=GOOGLE_API_KEY)

        # Configure HuggingFace warning
        os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        # Initialize Gemini model with direct API key
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0.7,
            google_api_key=GOOGLE_API_KEY,
            convert_system_message_to_human=True
        )

        # Updated memory configuration
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )

        self.vector_store = None

    def load_pdfs(self, pdf_paths: List[str]) -> None:
        """
        Load and process PDF documents into the vector store.

        Args:
            pdf_paths: List of paths to PDF files
        """
        documents = []
        for path in pdf_paths:
            if not os.path.exists(path):
                raise FileNotFoundError(f"PDF file not found: {path}")
            loader = PyPDFLoader(path)
            documents.extend(loader.load())

        # Split documents into chunks
        splits = self.text_splitter.split_documents(documents)

        # Create or update vector store
        if self.vector_store is None:
            self.vector_store = FAISS.from_documents(splits, self.embeddings)
        else:
            self.vector_store.add_documents(splits)

    def setup_rag_chain(self) -> None:
        """Set up the RAG chain with custom prompt template."""
        if not self.vector_store:
            raise ValueError("No documents loaded. Please load documents first.")

        # Create custom prompt templates
        system_template = """You are a helpful AI assistant powered by Google's Gemini model. 
        Use the following pieces of context to answer the user's question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Context: {context}
        ----------------
        Chat History: {chat_history}
        """

        messages = [
            SystemMessagePromptTemplate.from_template(system_template),
            HumanMessagePromptTemplate.from_template("{question}")
        ]

        prompt = ChatPromptTemplate.from_messages(messages)

        # Updated chain configuration
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vector_store.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 3}
            ),
            memory=self.memory,
            combine_docs_chain_kwargs={
                "prompt": prompt,
                "document_variable_name": "context"
            },
            return_source_documents=True,
            chain_type="stuff"
        )

    def query(self, question: str) -> str:
        """
        Query the RAG system with a question.

        Args:
            question: The question to ask

        Returns:
            str: The response from the model
        """
        if not hasattr(self, 'chain'):
            self.setup_rag_chain()

        response = self.chain.invoke({"question": question})
        return response["answer"]