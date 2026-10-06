import time
from app.services.model_loader import get_model,get_model_version
from app.metrics import PREDICTION_COUNTER, PREDICTION_LATENCY

def predict_category(description:str) ->dict:
    """Predict the category for an expense description"""
    start = time.time()
    model = get_model()
    prediction = model.predict([description])[0]
    category = str(prediction)

    elapsed = time.time() - start
    PREDICTION_LATENCY.observe(elapsed)
    PREDICTION_COUNTER.labels(category=category).inc()

    return {
        "description": description,
        "category": str(prediction),
        "model_version": get_model_version(),
    }