# 🩺 Breast Cancer Predictor App

Bu proje, meme kanseri teşhisi için çeşitli makine öğrenimi modelleri (Logistic Regression, Naive Bayes, KNN, SVM) kullanarak sınıflandırma yapan interaktif bir Streamlit uygulamasıdır. Kullanıcılar, uygulama üzerinden model seçimi yapabilir, görsel olarak sonuçları inceleyebilir ve çeşitli parametreleri ayarlayarak modeli test edebilirler.

🔗 [Canlı Uygulamayı Görüntüle](https://breastcancerpredictorsureyyaengin.streamlit.app/)

## 🚀 Özellikler

- Kullanıcı dostu arayüz (Streamlit ile geliştirildi)
- 4 farklı model arasında seçim yapma imkânı
- Canlı olarak tahmin sonucu ve olasılıkların gösterilmesi
- Eğitilen modeller `.pkl` dosyaları olarak yüklü
- Görsel analizler ve sınıflandırma sonuçları

## 📊 Kullanılan Veri Seti

- **Veri Seti:** Breast Cancer Wisconsin (Diagnostic) Data Set  
- **Kaynak:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/breast+Cancer+Wisconsin+(Diagnostic))
- **Özellikler:**
  - radius_mean, texture_mean, perimeter_mean, area_mean, vb.
  - Hedef: `diagnosis` (B = Benign, M = Malignant)

## 🧠 Kullanılan Modeller

1. **Logistic Regression**
2. **Naive Bayes**
3. **K-Nearest Neighbors (KNN)**
4. **Support Vector Machine (SVM)**

Modeller `model/train_models.py` dosyası ile eğitilir ve `model/*.pkl` dosyaları olarak kaydedilir.

## ⚙️ Kurulum

```bash
git clone https://github.com/kullaniciadi/breast-cancer-predictor.git
cd breast-cancer-predictor
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Proje Yapısı

├── app/                 # Streamlit uygulaması

│   └── main.py

├── assets/                

│   └── style.css

├── data/                #DataSet

│   └── data.csv

├── model/                #Model Eğitimi ve Modeller

│   ├── knn_model.pkl   

│   ├── knn_scaler.pkl

│   ├── logistic_model.pkl

│   ├── logistic_scaler.pkl

│   ├── main.py

│   ├── naive_bayes_model.pkl

│   ├── naive_bayes_scaler.pkl

│   ├── svm_model.pkl

│   └── svm_scaler.pkl

├── requirements.txt       # Gerekli paketler

└── README.md              # Proje tanımı



