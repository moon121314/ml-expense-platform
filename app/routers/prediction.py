"""Prediction and health endpoints."""
import time
from fastapi import APIRouter, HTTPException, status

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
    HealthResponse,
)
from app.services.predictor import predict_category
from app.metrics import PREDICTION_COUNTER, PREDICTION_LATENCY 


router = APIRouter(tags=["prediction"])


@router.get("/health", response_model=HealthResponse)
def health():
    """Health check endpoint."""
    return {"status": "ok"}


@router.post("/predict",response_model=PredictionResponse,status_code=status.HTTP_200_OK,)
def predict(payload: PredictionRequest):
    """Predict the expense category for a given description."""
    start_time = time.time()
    try:
        result = predict_category(payload.description)
        category = result.get("category") if isinstance(result, dict) else result
        PREDICTION_COUNTER.labels(category=category).inc()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {e}",
        )
    finally:
        duration = time.time() - start_time
        PREDICTION_LATENCY.observe(duration)
    return result