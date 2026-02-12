# crop-disease-monitoring-app
AI-powered Crop Disease Monitoring &amp; Prediction System (Web + PWA)
# 🌾 Crop Disease Monitoring & Prediction System

An AI-powered Crop Disease Monitoring & Prediction System that detects plant diseases from leaf images and provides prevention suggestions.  
The system works as a responsive web application and can be installed as a Progressive Web App (PWA) to function like a mobile app.

---

## 📌 Problem Statement

Crop diseases significantly reduce agricultural productivity and cause financial loss to farmers.  
Early detection of plant diseases can help farmers take preventive action and improve crop yield.

This project aims to:

- Detect crop diseases using image classification (Deep Learning)
- Provide treatment and prevention suggestions
- Work on both desktop and mobile devices
- Be simple, scalable, and production-ready

---

## 🎯 Project Objectives

- ✅ Build a deep learning model to classify crop diseases
- ✅ Develop a Flask-based backend API for prediction
- ✅ Create a responsive frontend UI
- ✅ Convert the web app into a Progressive Web App (PWA)
- ✅ Follow proper GitHub workflow with issues and PRs
- ✅ Practice team collaboration and project leadership

---

## 🏗️ System Architecture

### 🔄 High-Level Flow


+----------------------+
| User (Mobile/Web) |
+----------------------+
|
v
+----------------------+
| Frontend (HTML/CSS) |
| Responsive UI |
+----------------------+
|
v
+----------------------+
| Flask Backend API |
| /predict |
+----------------------+
|
v
+----------------------+
| ML Model (CNN) |
| TensorFlow / Keras |
+----------------------+
|
v
+----------------------+
| Prediction Result |
+----------------------+


---

## ⚙️ Technical Architecture

### 🖥 Frontend
- HTML
- CSS
- JavaScript
- Responsive Design
- PWA (Manifest + Service Worker)

### 🧠 Backend
- Python
- Flask
- REST API
- Image Processing

### 🤖 Machine Learning
- TensorFlow / Keras
- Convolutional Neural Network (CNN)
- Transfer Learning
- PlantVillage Dataset

### 🗄 Database (Optional Phase)
- SQLite (for storing prediction history)

---

## 📂 Project Structure

crop-disease-monitoring-app/
│
├── frontend/
│ ├── templates/
│ ├── static/
│ ├── manifest.json
│ └── service-worker.js
│
├── backend/
│ ├── app.py
│ ├── routes/
│ └── model/
│
├── ml_model/
│ ├── train.py
│ ├── dataset/
│ └── saved_model/
│
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore


---

## 🚀 Features (MVP Version 1)

- 📷 Upload crop leaf image  
- 🤖 AI-based disease prediction  
- 📊 Display confidence score  
- 💊 Show prevention suggestions  
- 📱 Mobile responsive UI  
- 📲 Installable as mobile app (PWA)  

---

## 📅 Development Roadmap (1 Month Plan)

### Week 1 – ML Model Development
- Dataset setup  
- Data preprocessing  
- Model training  
- Accuracy evaluation  
- Save trained model  

### Week 2 – Backend Development
- Setup Flask project  
- Create `/predict` endpoint  
- Integrate ML model  
- API testing  

### Week 3 – Frontend Development
- Responsive UI  
- Image upload feature  
- API integration  
- Display results  

### Week 4 – Integration & Deployment
- Convert to PWA  
- Bug fixes  
- Testing  
- Documentation  
- Deployment  

---

## 🌐 API Design

### POST `/predict`

**Request:**  
- Image file  

**Response (JSON):**

```json
{
  "disease": "Tomato Early Blight",
  "confidence": 92.4,
  "suggestion": "Apply appropriate fungicide and remove infected leaves."
}
```



## 🧪 Machine Learning Approach

The machine learning pipeline is designed to ensure accurate and efficient crop disease detection.

### 🔍 Data Preprocessing
- Image resizing to fixed input size (e.g., 224x224)
- Pixel normalization (scaling values between 0–1)
- Label encoding for classification

### 🔄 Data Augmentation
- Random rotation
- Horizontal & vertical flipping
- Zoom adjustments
- Brightness variation

This improves generalization and prevents overfitting.

### 🧠 Model Architecture
- Transfer Learning using **MobileNet / ResNet**
- Pre-trained ImageNet weights
- Custom classification head
- Softmax activation for multi-class prediction

### 📊 Model Evaluation
- Accuracy metric
- Loss monitoring
- Validation split
- Confusion matrix analysis (optional phase)

**🎯 Target Accuracy:** 85%+

---

## 🔒 Git Workflow Strategy

To maintain clean and scalable development:

### 🌿 Branch Structure
- `main` → Production-ready stable code  
- `dev` → Development branch  
- `feature/*` → Individual feature branches  



### 🔁 Development Process
1. Create a feature branch from `dev`
2. Implement changes
3. Open Pull Request (PR)
4. Code review by Project Lead
5. Merge into `dev`
6. After testing, merge `dev` → `main`

### 📌 Rules
- No direct push to `main`
- Every task must be linked to an Issue
- Clear commit messages required

---

## 👥 Team Roles & Responsibilities

### Project Lead & Backend Developer
- System architecture design  
- Backend API development  
- ML model integration  
- Code review & approval  
- Project management & sprint planning  

### 🤖 ML Engineer
- Dataset preparation  
- Data preprocessing pipeline  
- Model training & tuning  
- Performance optimization  

### 🌐 Frontend Developer
- UI/UX design  
- Responsive layout development  
- API integration  
- PWA implementation  

---

## 📦 Future Enhancements

Planned improvements after MVP completion:

- 🌍 Multi-language support (Hindi & English)
- 📍 Geo-location tagging of predictions
- 📊 Disease analytics dashboard
- ☁ Cloud deployment (AWS / GCP)
- 📱 Native Android/iOS app
- 📈 Historical prediction tracking

---

## 🛡 Contribution Guidelines

To ensure clean collaboration:

- Create a feature branch for new work  
- Follow commit message conventions  
- Reference issue number in commits  
- No direct push to `main`  
- Pull Request required before merge  

### ✅ Commit Format Example


---

## 📄 License

This project is licensed under the **MIT License**.

---

