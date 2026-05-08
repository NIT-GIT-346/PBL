from fastapi import APIRouter, Depends
from mock_data.pipeline import PIPELINE_STATUS
from services.kafka_simulator import kafka_service
from utils.auth import get_current_user

router = APIRouter()


@router.get("/pipeline-status")
async def get_pipeline_status(current_user: dict = Depends(get_current_user)):
    kafka_stats = kafka_service.get_stats()
    return {
        "components": PIPELINE_STATUS,
        "kafka": kafka_stats,
    }
