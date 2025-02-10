import streamlit as st
from RAGAgent import RAGAgent
import os

# Set page configuration
st.set_page_config(
    page_title="PDF Soru-Cevap Sistemi",
    page_icon="📚",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .upload-text {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'rag_agent' not in st.session_state:
    st.session_state.rag_agent = None
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []

# Title and description
st.title("📚 PDF Soru-Cevap Sistemi")
st.markdown("---")

# Sidebar for PDF upload
with st.sidebar:
    st.header("📄 PDF Yükleme")
    uploaded_files = st.file_uploader(
        "PDF dosyalarınızı yükleyin",
        type=['pdf'],
        accept_multiple_files=True
    )

    if uploaded_files:
        if uploaded_files != st.session_state.uploaded_files:
            # Save uploaded files
            saved_paths = []
            for uploaded_file in uploaded_files:
                # Create temp directory if it doesn't exist
                if not os.path.exists('temp'):
                    os.makedirs('temp')

                # Save the file
                file_path = os.path.join('temp', uploaded_file.name)
                with open(file_path, 'wb') as f:
                    f.write(uploaded_file.getbuffer())
                saved_paths.append(file_path)

            # Initialize RAG agent with uploaded files
            try:
                st.session_state.rag_agent = RAGAgent()
                st.session_state.rag_agent.load_pdfs(saved_paths)
                st.session_state.uploaded_files = uploaded_files
                st.success("PDF dosyaları başarıyla yüklendi! 🎉")
            except Exception as e:
                st.error(f"Hata oluştu: {str(e)}")

# Main content area
if st.session_state.rag_agent is None:
    st.info("👈 Başlamak için lütfen soldaki menüden PDF dosyası yükleyin.")
else:
    # Question input
    question = st.text_input("🤔 Sorunuzu yazın:", placeholder="PDF içeriği hakkında bir soru sorun...")

    if st.button("Cevapla", type="primary"):
        if question:
            try:
                with st.spinner("Cevap hazırlanıyor..."):
                    response = st.session_state.rag_agent.query(question)

                # Display response in a nice format
                st.markdown("### 💡 Cevap:")
                st.markdown(response)
            except Exception as e:
                st.error(f"Bir hata oluştu: {str(e)}")
        else:
            st.warning("Lütfen bir soru girin.")

# Footer
st.markdown("---")
st.markdown("*Bu uygulama Google Gemini ve FAISS kullanılarak geliştirilmiştir.*")