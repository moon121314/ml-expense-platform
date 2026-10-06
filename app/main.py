from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

from app.routers import prediction
from app.services.model_loader import load_model


app = FastAPI(title="ML Expense Platform", version="1.0.0")

@app.on_event("startup")
def startup_event() -> None:
    load_model()


@app.get("/metrics")
def metrics():
    """Expose Prometheus metrics."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


app.include_router(prediction.router)