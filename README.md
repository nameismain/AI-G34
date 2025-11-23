<h1 align="center">💳 Loan Approval Prediction · ML Classification Project</h1>
<p align="center">
  <b>ITE351 – AI & Applications · Group 34</b><br>
  <i>Hanyang University, Fall 2025</i><br>
  <a href="https://nameismain.github.io/AI-G34/">🌐 Live Site</a> · 
  <a href="https://www.notion.so/taehyun-kim/ITE351-Group-Project-Blog-2b4098f461e08018a462e4bfd5797a25?source=copy_link">🧠 Notion Workspace</a>
</p>

---

## 📌 Overview

This project explores how machine learning can support loan approval decisions by analyzing financial, demographic, and credit-related information from applicants.

Using a structured dataset of **45,000 records** from Kaggle  
(“Loan Approval Classification Data”), we build and evaluate models that classify whether a loan application will be **approved (1)** or **rejected (0)**.

> 🎯 *Goal: Understand which features matter most and build a reliable ML classifier for loan decisions.*

---

## 🎯 Objectives

- Perform **EDA** to understand the dataset and feature relationships  
- Apply **preprocessing** including outlier handling, encoding, and scaling  
- Train multiple **classification models**  
- Compare performance using common ML metrics  
- Interpret feature importance and relate results to real-world lending logic  

---

## 🧪 Methodology

### 1️⃣ Data Loading & Inspection
- Load CSV dataset from Kaggle  
- Examine structure, datatypes, missing values (none), and initial distributions  
- Identify numeric vs. categorical features  

### 2️⃣ Exploratory Data Analysis (EDA)
- Histogram and boxplot analysis  
- Target variable imbalance check  
- Categorical feature distributions  
- Loan status by category (gender, education, home ownership, loan intent, defaults)  
- Numeric feature comparison (income, credit score, loan amount, interest rate)  
- Correlation heatmap  

### 3️⃣ Preprocessing & Feature Engineering
- Remove obviously unrealistic outliers (e.g., age > 100)  
- Apply clipping to extreme values (income, loan amount)  
- One-hot encode categorical variables  
- Train-test split  
- Optional normalization depending on algorithm  

### 4️⃣ Model Development
We evaluate several classifiers:

| Model | Notes |
|-------|--------|
| Logistic Regression | Baseline linear model |
| Random Forest | Non-linear, handles interactions well |
| XGBoost | High performance gradient boosting model |

Metrics used:  
**Accuracy, Precision, Recall, F1-score, ROC-AUC**

### 5️⃣ Evaluation & Interpretation
- Compare model performance  
- Analyze feature importance from tree-based models  
- Key predictors include:  
  - **Credit Score** (higher score → higher approval probability)  
  - **Loan Percent Income** (higher ratio → more rejections)  
  - **Past Defaults** (previous default almost always → rejection)  
  - **Home Ownership**  

---

## 📂 Repository Structure
```
loan-approval-prediction/
│── data/
│   ├── raw/
│   └── processed/
│── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_evaluation.ipynb
│── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── evaluate.py
│   └── utils.py
│── results/
│── models/
│── README.md
│── index.html
```

## 🧠 Tech Stack

| Category | Tools |
|----------|-------|
| **Programming** | Python |
| **Data Analysis** | pandas · NumPy |
| **Visualization** | Matplotlib · Seaborn |
| **Machine Learning** | Scikit-Learn · XGBoost |
| **Dev / Docs** | GitHub · GitHub Pages · Notion |

---

## 👥 Team 34

| Name | Department | Contact |
|------|-------------|----------|
| **Minjin Kim** | Information Systems | idid02@hanyang.ac.kr |
| **Taehyun Kim** | Computer Science | tanggu01@connect.hku.hk |
| **Lison Olympie** | Computer Science | lsn.olmp@gmail.com |
| **Tom Georgin** | Computer Science | tom@georgin.net |

---

<p align="center">
  <sub>📅 Last updated: November 2025</sub><br>
</p>
