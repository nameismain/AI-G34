import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import shap

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SAVE_DIR = os.path.join(BASE_DIR, "results", "feature_importance")
os.makedirs(SAVE_DIR, exist_ok=True)

def save_random_forest_importance(model, feature_names):
    df = pd.DataFrame({
        "feature": feature_names,
        "importance": model["model"].feature_importances_
    }).sort_values("importance", ascending=False)

    df.to_csv(os.path.join(SAVE_DIR, "random_forest_importance.csv"), index=False)

    plt.figure(figsize=(10, 8))
    plt.barh(df["feature"], df["importance"])
    plt.title("Random Forest Feature Importance")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(SAVE_DIR, "random_forest_importance.png"))
    plt.close()
    

def save_xgboost_importance(model, feature_names):
    df = pd.DataFrame({
        "feature": feature_names,
        "importance": model["model"].feature_importances_
    }).sort_values("importance", ascending=False)

    df.to_csv(os.path.join(SAVE_DIR, "xgboost_importance.csv"), index=False)

    plt.figure(figsize=(10, 8))
    plt.barh(df["feature"], df["importance"])
    plt.title("XGBoost Feature Importance")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(SAVE_DIR, "xgboost_importance.png"))
    plt.close()
    

def save_shap_values(model, X_train_transformed, feature_names):
    explainer = shap.TreeExplainer(model["model"])
    shap_values = explainer.shap_values(X_train_transformed)

    plt.figure(figsize=(10, 8))
    shap.summary_plot(shap_values, X_train_transformed,
                      feature_names=feature_names,
                      show=False)
    plt.tight_layout()
    plt.savefig(os.path.join(SAVE_DIR, "shap_summary.png"))
    plt.close()

    np.save(os.path.join(SAVE_DIR, "shap_values.npy"), shap_values)
