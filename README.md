<<<<<<< HEAD
# 📚 PDF Question-Answering System
=======
# 📚 PDF Soru-Cevap Sistemi
>>>>>>> f6240584bad4d017a6d89ec7f49aae3bfa06b27d

A RAG (Retrieval-Augmented Generation) based question-answering system that allows you to upload PDF documents and ask questions about their contents. Built using Google Gemini AI and FAISS.

<<<<<<< HEAD
## ✨ Features

- 📄 Support for multiple PDF file uploads
- 🎯 User-friendly Streamlit interface
- 🤖 Google Gemini AI powered natural language processing
- 🚀 Fast document search using FAISS vector database
- 🌍 Multi-language support

## 🛠️ Installation
=======
## ✨ Özellikler

- 📄 Çoklu PDF dosyası yükleme desteği
- 🎯 Kullanıcı dostu Streamlit arayüzü
- 🤖 Google Gemini AI tabanlı doğal dil işleme
- 🚀 FAISS vektör veritabanı ile hızlı belge araması
- 🇹🇷 Türkçe dil desteği

## 🛠️ Kurulum
>>>>>>> f6240584bad4d017a6d89ec7f49aae3bfa06b27d

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

<<<<<<< HEAD
## 🚀 Usage
=======
## 🚀 Kullanım
>>>>>>> f6240584bad4d017a6d89ec7f49aae3bfa06b27d

1. Start the application:
```bash
streamlit run main.py
```

<<<<<<< HEAD
2. In the web browser that automatically opens:
   - 📂 Upload your PDF files from the left sidebar
   - ✍️ Type your question in the text box
   - 🔍 Click the "Answer" button

## 📋 Requirements

- 🐍 Python 3.8+
- 🔑 Google Gemini API key
- 📦 All packages listed in requirements.txt

## 🔧 Technical Stack
=======
2. Web tarayıcınızda otomatik olarak açılan uygulamada:
   - 📂 Sol menüden PDF dosyalarınızı yükleyin
   - ✍️ Metin kutusuna sorunuzu yazın
   - 🔍 "Cevapla" butonuna tıklayın

## 📋 Gereksinimler

- 🐍 Python 3.8+
- 🔑 Google Gemini API anahtarı
- 📦 requirements.txt'de listelenen tüm paketler

## 📜 Lisans
>>>>>>> f6240584bad4d017a6d89ec7f49aae3bfa06b27d

- Streamlit for the web interface
- LangChain for RAG implementation
- Google Gemini AI for language processing
- FAISS for vector similarity search
- Sentence Transformers for embeddings

<<<<<<< HEAD
## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. 🔱 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request 
=======
## 🤝 Katkıda Bulunma

1. 🔱 Bu repository'yi fork edin
2. 🌿 Feature branch'inizi oluşturun (`git checkout -b feature/AmazingFeature`)
3. 💾 Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. 🔄 Bir Pull Request oluşturun 
>>>>>>> f6240584bad4d017a6d89ec7f49aae3bfa06b27d
