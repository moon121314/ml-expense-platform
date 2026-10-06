"""Training pipeline for expense categorization with MLflow tracking."""
import os

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


mlflow.set_tracking_uri(
    "sqlite:////Users/moon/Downloads/Python/Day13/ml-expense-platform/mlflow.db"
)

DATA_PATH = "/Users/moon/Downloads/Python/Day13/ml-expense-platform/ml/data/raw/sample_expenses.csv"
MODEL_PATH = "/Users/moon/Downloads/Python/Day13/ml-expense-platform/ml/models/model.pkl"
EXPERIMENT_NAME = "expense-categorization"


def load_data(path: str) -> pd.DataFrame:
    """Load the training data from CSV."""
    return pd.read_csv(path)


def build_pipeline(C: float = 1.0) -> Pipeline:
    """Create a text classification pipeline."""
    return Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
        ("clf", LogisticRegression(C=C, max_iter=500, random_state=42)),
    ])


def train(C: float = 1.0) -> None:
    """Train, evaluate, and log the model with MLflow."""
    mlflow.set_experiment(EXPERIMENT_NAME)

    df = load_data(DATA_PATH)
    X = df["description"]
    y = df["category"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y,
    )

    with mlflow.start_run() as run:
        pipeline = build_pipeline(C=C)
        pipeline.fit(X_train, y_train)

        preds = pipeline.predict(X_test)
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, average="weighted")

        mlflow.log_param("C", C)
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("vectorizer", "tfidf_ngram_1_2")
        mlflow.log_param("model", "logistic_regression")

        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_weighted", f1)

        mlflow.sklearn.log_model(pipeline, name="model")

        print(f"Run ID: {run.info.run_id}")
        print(f"C: {C}")
        print(f"Accuracy: {acc:.4f}")
        print(f"F1 (weighted): {f1:.4f}")

        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        joblib.dump(pipeline, MODEL_PATH)
        print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    for C in [0.01, 0.1, 1.0, 10.0]:
        train(C=C)
        print("-" * 40)