# 📚 RAGMind Agent: AI-Driven Knowledge Extraction from PDF

A RAG (Retrieval-Augmented Generation) based question-answering system that allows you to upload PDF documents and ask questions about their contents. Built using Google Gemini AI and FAISS.

## ✨ Features
  
- 📄 Support for multiple PDF file uploads
- 🎯 User-friendly Streamlit interface
- 🤖 Google Gemini AI powered natural language processing
- 🚀 Fast document search using FAISS vector database
- 🌍 Multi-language support

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/altantopbas/PDF_QA_RAG.git
cd PDF_QA_RAG
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Google Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## 🚀 Usage

1. Start the application:
```bash
streamlit run main.py
```

2. In the web browser that automatically opens:
   - 📂 Upload your PDF files from the left sidebar
   - ✍️ Type your question in the text box
   - 🔍 Click the "Answer" button
  
3. Usage Example:
   - ![Usage Example Demo](https://github.com/altantopbas/PDF_QA_RAG/blob/main/example.gif)

## 📋 Requirements

- 🐍 Python 3.8+
- 🔑 Google Gemini API key
- 📦 All packages listed in requirements.txt

## 🔧 Technical Stack

- 🌐 Streamlit for the web interface
- 🦜️🔗 LangChain for RAG implementation
- 🧠 Google Gemini AI for language processing
- 🔍 FAISS for vector similarity search
- 🔄 Sentence Transformers for embeddings

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. 🔱 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request 
