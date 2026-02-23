# fraud-detection-ml
Machine learning-based fraud detection system with EDA, feature engineering, and a Streamlit web application for real-time prediction.

---

## 🚀 Project Overview

Fraud detection is a binary classification problem where:

- `0` → Legitimate Transaction  
- `1` → Fraudulent Transaction  

The goal is to identify fraudulent transactions using transaction-related features.

---

## 📊 Dataset

This project uses the Fraud Detection Dataset from Kaggle:

https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset

---

## 🧠 Features Used

- Transaction Type
- Transaction Amount
- Old Balance (Sender)
- New Balance (Sender)
- Old Balance (Receiver)
- New Balance (Receiver)

Additional engineered features were created during analysis.

---

## 🔍 Exploratory Data Analysis (EDA)

During the analysis phase:

- Fraud rate was examined (class imbalance detected)
- Fraud distribution across transaction types analyzed
- Transaction amount distribution visualized
- Balance inconsistencies explored
- Suspicious transaction patterns identified

---

## 🤖 Model

Model Type:
- Logistic Regression (or update with your actual model)

Techniques Used:
- Train-Test Split
- Feature Encoding
- Scaling
- Pipeline Implementation

Evaluation Metrics:
- Accuracy
- Precision
- Recall
- ROC-AUC

---

## 🌐 Streamlit Web Application

The project includes a Streamlit interface where users can:

- Enter transaction details
- Predict if the transaction is fraudulent
- View prediction results instantly

---
