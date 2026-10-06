import joblib

from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[2] / "ml" / "models" / "model.pkl"
MODEL_VERSION = "v1"

_model = None

def load_model() -> None:
    global _model
    _model = joblib.load(MODEL_PATH)

def get_model():
    """return the loaded model .raises if not loaded"""
    if _model is None:
        raise RuntimeError("Model not loaded.Call load_model() first")
    return _model

def get_model_version() -> str:
    """Return the current model version string"""
    return MODEL_VERSION