from fastapi import APIRouter, Depends
from services.cache import cache_json_get, cache_json_set
from mock_data.metrics import MODEL_METRICS, DRL_TRAINING_DATA, CONFUSION_MATRIX
from utils.auth import get_current_user

router = APIRouter()


@router.get("/model-metrics")
async def get_model_metrics(current_user: dict = Depends(get_current_user)):
    cached = await cache_json_get("model_metrics")
    if cached:
        return cached

    data = {
        "models": MODEL_METRICS,
        "training_data": DRL_TRAINING_DATA,
        "confusion_matrix": CONFUSION_MATRIX,
    }
    await cache_json_set("model_metrics", data, ttl=300)
    return data
