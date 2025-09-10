from fastapi import APIRouter
from pydantic import BaseModel
from app.api.v1.fraud_engine import RealTimeFeatureEngine

router = APIRouter()

class Transaction(BaseModel):
    user_id: str
    amount: float

@router.post("/fraud")
def predict(transaction: Transaction):
    engine = RealTimeFeatureEngine(redis_client=None)
    features = engine.compute_features(transaction.model_dump())

    # Calculo dummy de score (ajuste depois com modelo de ML real)
    risk_score = round(abs(features["amount_zscore"]) / 3, 2)

    return {
        "fraud": risk_score > 0.7,  # regra de exemplo
        "risk_score": risk_score,
        "features": features
    }
