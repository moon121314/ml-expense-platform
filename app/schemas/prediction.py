from pydantic import BaseModel,Field


class PredictionRequest(BaseModel):
    """What the client sends to predict"""
    description:str = Field(min_length=1,max_length=200,description="Expense description,eg 'Starbucks latte'",examples=["Starbucks latte"],)


class PredictionResponse(BaseModel):
    """what / predict sends back"""

    description: str
    category: str
    model_version: str


class HealthResponse(BaseModel):
    """What /health sends back."""
    status: str