import joblib
from pathlib import Path

MODEL_DIR = Path("trained_models")


def load_model(model_name: str):
    model_path = MODEL_DIR / model_name

    if not model_path.exists():
        raise FileNotFoundError(f"Model not found: {model_path}")

    return joblib.load(model_path)
