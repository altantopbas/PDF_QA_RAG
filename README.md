# 📚 PDF Soru-Cevap Sistemi

Bu proje, PDF dosyalarını yükleyip içerikleri hakkında sorular sorabileceğiniz bir RAG (Retrieval-Augmented Generation) tabanlı soru-cevap sistemidir. Google Gemini AI ve FAISS kullanılarak geliştirilmiştir.

## ✨ Özellikler

- 📄 Çoklu PDF dosyası yükleme desteği
- 🎯 Kullanıcı dostu Streamlit arayüzü
- 🤖 Google Gemini AI tabanlı doğal dil işleme
- 🚀 FAISS vektör veritabanı ile hızlı belge araması
- 🇹🇷 Türkçe dil desteği

## 🛠️ Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/altantopbas/PDF_QA_RAG.git
cd PDF_QA_RAG
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. `.env` dosyası oluşturun ve Google Gemini API anahtarınızı ekleyin:
```
GEMINI_API_KEY=your_api_key_here
```

## 🚀 Kullanım

1. Uygulamayı başlatın:
```bash
streamlit run main.py
```

2. Web tarayıcınızda otomatik olarak açılan uygulamada:
   - 📂 Sol menüden PDF dosyalarınızı yükleyin
   - ✍️ Metin kutusuna sorunuzu yazın
   - 🔍 "Cevapla" butonuna tıklayın

## 📋 Gereksinimler

- 🐍 Python 3.8+
- 🔑 Google Gemini API anahtarı
- 📦 requirements.txt'de listelenen tüm paketler

## 📜 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🤝 Katkıda Bulunma

1. 🔱 Bu repository'yi fork edin
2. 🌿 Feature branch'inizi oluşturun (`git checkout -b feature/AmazingFeature`)
3. 💾 Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. 🔄 Bir Pull Request oluşturun 
