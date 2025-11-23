import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def preprocess_data(df):
    df = df.copy()
    # Drop unrealistic age values
    df = df[df["person_age"] <= 100]

    # Target variable encoding
    df["loan_status"] = df["loan_status"].map({"Yes": 1, "No": 0, 1: 1, 0: 0})

    # Features / target split
    X = df.drop("loan_status", axis=1)
    y = df["loan_status"]

    # Identify categorical and numeric columns
    categorical_cols = X.select_dtypes(include=["object"]).columns
    numeric_cols = X.select_dtypes(exclude=["object"]).columns

    # Preprocessing transformers
    numeric_transformer = StandardScaler()

    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_cols),
            ("cat", categorical_transformer, categorical_cols),
        ]
    )

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test, preprocessor