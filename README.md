
# 📊 Loan Approval Prediction

Short description: This repository contains a complete end-to-end machine learning pipeline for predicting loan approval outcomes (approved = 1 / rejected = 0). It includes EDA, preprocessing, model training (Logistic Regression, Random Forest, XGBoost), evaluation, interpretability (SHAP), and an academic-style report.

**Project:** ITE351 Group 34 — Hanyang University (Fall 2025)

[Notion Workspace](https://www.notion.so/taehyun-kim/ITE351-Group-Project-Blog-2b4098f461e08018a462e4bfd5797a25?source=copy_link)

---

## Table of Contents
- [Key Features](#key-features)
- [Data](#data)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Reproducibility](#reproducibility)
- [Results & Evaluation](#results--evaluation)
- [Notebooks & Documentation](#notebooks--documentation)
- [Team & Contact](#team--contact)
- [Contributing](#contributing)
- [License](#license)

---

## Key Features
- **Data loading & preprocessing:** Reproducible preprocessing pipeline including missing value handling, categorical encoding, and scaling (`src/preprocessing.py`).
- **Model comparison:** Train and compare Logistic Regression, Random Forest, and XGBoost (`src/train_model.py`).
- **Evaluation:** Common metrics (accuracy, precision, recall, F1, ROC-AUC) and visualizations (`src/evaluate.py`).
- **Interpretability:** Feature importance and SHAP analysis to explain model predictions (`src/feature_importance.py`).
- **Reproducible notebooks:** Step-by-step Jupyter notebooks for EDA → preprocessing → modeling → evaluation (`notebooks/`).

## Data
- Raw dataset: `data/raw/loan_data.csv`
- Processed data: `data/processed/cleaned_data.csv`, `X_train.npy`, `X_test.npy`, `y_train.npy`, `y_test.npy`

See `notebooks/02_preprocessing.ipynb` for column descriptions and preprocessing details.

## Project Structure
```
loan-approval-prediction/
├─ README.md
├─ run.py                 # Orchestrator for the full pipeline
├─ requirements.txt
├─ data/
│  ├─ raw/
│  └─ processed/
├─ notebooks/             # EDA / preprocessing / modeling / evaluation
├─ src/                   # Reusable pipeline modules
└─ results/               # Visualizations and metric outputs
```

## Installation
1. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. (Optional, macOS) If you plan to use XGBoost
```bash
brew install libomp
```

## Quick Start
- Run the full pipeline
```bash
python3 run.py
```
This script runs data loading → preprocessing → model training → evaluation and saves artifacts (models: `models/`, visualizations: `results/`).

- Run individual steps (for example, training or evaluation)
```bash
python3 src/train_model.py
python3 src/evaluate.py
```

## Reproducibility
1. Set up the virtual environment and install dependencies
2. Place the raw dataset at `data/raw/loan_data.csv`
3. Run `python3 run.py` to produce `models/` and `results/`

Hyperparameters and additional options are available at the top of `src/train_model.py`.

## Results & Evaluation
- Results directory: `results/` (contains EDA figures, feature importance, metrics, etc.)
- Summary performance:

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|------:|---------:|----------:|-------:|---:|--------:|
| Logistic Regression | 0.899 | 0.785 | 0.749 | 0.767 | 0.956 |
| Random Forest       | 0.930 | 0.900 | 0.770 | 0.830 | 0.974 |
| XGBoost             | 0.934 | 0.896 | 0.796 | 0.843 | 0.979 |

Best performing model: **XGBoost**

Interpretability highlights: previous defaults, debt-to-income ratio (DTI), interest rate, income, and credit score are among the most influential features. SHAP visualizations are saved in `results/feature_importance/`.

## Notebooks & Documentation
- Reproducible notebooks: `notebooks/01_eda.ipynb`, `02_preprocessing.ipynb`, `03_modeling.ipynb`, `04_evaluation.ipynb`
- Academic report (LaTeX): `docs/paper.tex`, PDF: `docs/paper.pdf`

## Team & Contact
- Group 34 — Hanyang University, ITE351
- Team members: Minjin Kim, Taehyun Kim, Lison Olympie, Tom Georgin

For project-related questions, please open an issue in this repository or contact the maintainers.

## Contributing
- Report bugs or request features via issues. Code contributions are welcome via pull requests.

## License
- This repository is shared for educational purposes. Please contact the team before using the code or data for commercial purposes.
