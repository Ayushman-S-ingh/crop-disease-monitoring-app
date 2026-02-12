# 🛠 Developer Setup Guide

This guide helps team members set up the development environment properly.

---

## 📌 Prerequisites

Make sure you have installed:

- Python 3.10+
- pip
- Git
- VS Code (recommended)

---

## 🐍 Step 1: Clone the Repository

git clone https://github.com/YOUR_USERNAME/crop-disease-monitoring-app.git
cd crop-disease-monitoring-app


---

## 🌿 Step 2: Switch to Development Branch

git checkout dev
git pull


---

## 🧪 Step 3: Create Virtual Environment

python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows


---

## 📦 Step 4: Install Dependencies

For ML:

pip install -r ml_model/requirements.txt


For Backend:

pip install -r backend/requirements.txt


---

## 🚀 Running the Backend

cd backend
python app.py


Backend should start on:
http://127.0.0.1:5000

---

## 🧠 Running ML Training

cd ml_model
python train.py


---

# 🌿 Branch Workflow

Before starting any task:

git checkout dev
git pull
git checkout -b feature/task-name


After completing task:

git add .
git commit -m "feat: short description (#issue-number)"
git push origin feature/task-name


Then create Pull Request → dev branch.

---

# 📊 Board Workflow

When you start task:
Move issue → In Progress

When PR created:
Move issue → In Review

When merged:
Move issue → Done
🔥 Now Modify README Slightly
At bottom of README add:

## 🛠 Development Guide

For detailed setup instructions, see:
[Developer Setup Guide](SETUP.md)
