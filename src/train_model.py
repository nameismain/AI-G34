from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
import joblib
import os

def train_models(preprocessor, X_train, y_train, save_path="../models/"):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    models = {
        "logistic_regression": LogisticRegression(max_iter=500),
        "random_forest": RandomForestClassifier(n_estimators=150),
        "xgboost": XGBClassifier(
            n_estimators=200,
            learning_rate=0.1,
            max_depth=6,
            eval_metric="logloss"
        ),
    }

    trained_models = {}

    for name, model in models.items():
        pipe = Pipeline(steps=[("preprocess", preprocessor), ("model", model)])
        pipe.fit(X_train, y_train)

        joblib.dump(pipe, os.path.join(save_path, f"{name}.pkl"))
        trained_models[name] = pipe

    return trained_models