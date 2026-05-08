import logging
from fastapi import APIRouter, Depends
from schemas.patient import PatientInput, DiagnosisOutput, PatientCaseResponse
from services.ai_engine import analyze_patient
from services.cache import cache_json_get, cache_json_set
from services.kafka_simulator import kafka_service
from mock_data.cases import RECENT_CASES
from utils.auth import get_current_user

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/analyze-patient", response_model=DiagnosisOutput)
async def analyze_patient_endpoint(
    patient: PatientInput,
    current_user: dict = Depends(get_current_user),
):
    logger.info(f"Received patient analysis request: age={patient.age}, gender={patient.gender}")

    result = await analyze_patient(
        age=patient.age,
        gender=patient.gender,
        bp=patient.bp,
        heart_rate=patient.heart_rate,
        blood_sugar=patient.blood_sugar,
        temperature=patient.temperature,
        symptoms=patient.symptoms,
        history=patient.history,
    )

    await kafka_service.produce_message(
        "diagnosis-events",
        {
            "patient_age": patient.age,
            "condition": result["condition"],
            "risk_level": result["risk_level"],
        },
    )

    await cache_json_set(f"latest_diagnosis_{patient.age}_{patient.gender}", result, ttl=600)

    return DiagnosisOutput(**result)


@router.get("/recent-cases", response_model=list[PatientCaseResponse])
async def get_recent_cases(current_user: dict = Depends(get_current_user)):
    cached = await cache_json_get("recent_cases")
    if cached:
        return cached

    await cache_json_set("recent_cases", RECENT_CASES, ttl=120)
    return RECENT_CASES
