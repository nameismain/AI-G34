from src.data_loader import load_raw_data
from src.preprocessing import preprocess_data
from src.train_model import train_models
from src.evaluate import evaluate_models

from src.feature_importance import (
    save_random_forest_importance,
    save_xgboost_importance,
    save_shap_values
)


def main():
    print("📌 Loading data...")
    df = load_raw_data()

    print("📌 Preprocessing...")
    X_train, X_test, y_train, y_test, preprocessor = preprocess_data(df)

    print("📌 Training models...")
    models = train_models(preprocessor, X_train, y_train)

    print("📌 Evaluating models...")
    results = evaluate_models(models, X_test, y_test)
    print("\n===== Final Results =====\n")
    print(results)

    print("\n📌 Saving Feature Importances...")
    
    feature_names = preprocessor.get_feature_names_out()

    # Random Forest
    save_random_forest_importance(
        {"model": models["random_forest"].named_steps["model"]},
        feature_names
    )

    # XGBoost
    save_xgboost_importance(
        {"model": models["xgboost"].named_steps["model"]},
        feature_names
    )

    # SHAP — use XGBoost features
    import numpy as np
    X_train_transformed = models["xgboost"].named_steps["preprocess"].transform(X_train)

    save_shap_values(
        {"model": models["xgboost"].named_steps["model"]},
        X_train_transformed,
        feature_names
    )

    print("Feature importance saved successfully!")


if __name__ == "__main__":
    main()