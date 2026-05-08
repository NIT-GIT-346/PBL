import random
import asyncio
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

CONDITION_MAP: Dict[str, Dict] = {
    "cardiac": {
        "conditions": [
            "Acute Coronary Syndrome",
            "Atrial Fibrillation",
            "Hypertensive Crisis",
            "Congestive Heart Failure",
        ],
        "tests": [
            "Troponin I/T",
            "ECG 12-Lead",
            "Echocardiogram",
            "BNP/NT-proBNP",
            "Cardiac CT Angiography",
        ],
        "treatments": [
            "Administer aspirin 325mg STAT",
            "Start IV heparin drip per protocol",
            "Continuous cardiac monitoring",
            "Cardiology consult within 2 hours",
            "Serial troponin measurements q6h",
        ],
    },
    "respiratory": {
        "conditions": [
            "Community-Acquired Pneumonia",
            "Acute Bronchitis",
            "COPD Exacerbation",
            "Pulmonary Embolism",
        ],
        "tests": [
            "Chest X-Ray PA/Lateral",
            "CT Pulmonary Angiography",
            "Arterial Blood Gas",
            "Sputum Culture",
            "D-Dimer",
        ],
        "treatments": [
            "Initiate empiric antibiotic therapy",
            "Supplemental oxygen to maintain SpO2 > 94%",
            "Nebulized bronchodilator therapy",
            "Pulmonology consult",
            "Monitor respiratory rate and oxygen saturation",
        ],
    },
    "metabolic": {
        "conditions": [
            "Type 2 Diabetes - Uncontrolled",
            "Diabetic Ketoacidosis",
            "Metabolic Syndrome",
            "Hypoglycemia",
        ],
        "tests": [
            "HbA1c",
            "Comprehensive Metabolic Panel",
            "Fasting Lipid Panel",
            "Urinalysis with Microalbumin",
            "C-Peptide Level",
        ],
        "treatments": [
            "Initiate insulin sliding scale",
            "IV fluid resuscitation with normal saline",
            "Monitor blood glucose every 2 hours",
            "Endocrinology consult",
            "Dietary counseling and education",
        ],
    },
    "neurological": {
        "conditions": [
            "Ischemic Stroke",
            "Transient Ischemic Attack",
            "Migraine with Aura",
            "Meningitis",
        ],
        "tests": [
            "CT Head without Contrast",
            "MRI Brain with DWI",
            "Lumbar Puncture",
            "EEG",
            "Carotid Doppler Ultrasound",
        ],
        "treatments": [
            "Activate stroke protocol",
            "Assess for tPA eligibility (within 4.5 hours)",
            "Neurology consult STAT",
            "NPO until swallow evaluation",
            "Serial neurological assessments q1h",
        ],
    },
    "general": {
        "conditions": [
            "Systemic Inflammatory Response Syndrome",
            "Sepsis",
            "Acute Viral Infection",
            "Autoimmune Flare",
        ],
        "tests": [
            "Complete Blood Count with Differential",
            "Blood Cultures x2",
            "Procalcitonin",
            "ESR and CRP",
            "Lactate Level",
        ],
        "treatments": [
            "Initiate broad-spectrum antibiotics",
            "IV fluid bolus 30 mL/kg",
            "Continuous vital sign monitoring",
            "Infectious disease consult",
            "Reassess within 1 hour of intervention",
        ],
    },
}

SYMPTOM_CATEGORY_MAP = {
    "chest_pain": "cardiac",
    "palpitations": "cardiac",
    "shortness_of_breath": "respiratory",
    "cough": "respiratory",
    "wheezing": "respiratory",
    "frequent_urination": "metabolic",
    "excessive_thirst": "metabolic",
    "blurred_vision": "metabolic",
    "headache": "neurological",
    "dizziness": "neurological",
    "confusion": "neurological",
    "numbness": "neurological",
    "fever": "general",
    "fatigue": "general",
    "nausea": "general",
    "weight_loss": "general",
    "joint_pain": "general",
    "abdominal_pain": "general",
}


def _determine_category(symptoms: List[str], history: List[str]) -> str:
    category_scores: Dict[str, int] = {k: 0 for k in CONDITION_MAP}
    for symptom in symptoms:
        cat = SYMPTOM_CATEGORY_MAP.get(symptom, "general")
        category_scores[cat] += 2
    history_map = {
        "diabetes": "metabolic",
        "hypertension": "cardiac",
        "heart_disease": "cardiac",
        "asthma": "respiratory",
        "copd": "respiratory",
        "stroke": "neurological",
        "epilepsy": "neurological",
    }
    for h in history:
        cat = history_map.get(h, "general")
        category_scores[cat] += 1
    return max(category_scores, key=category_scores.get)


def _calculate_risk(age: int, heart_rate: int, blood_sugar: float, bp: str, temperature: float) -> str:
    risk_score = 0
    if age > 65:
        risk_score += 3
    elif age > 50:
        risk_score += 2
    elif age > 35:
        risk_score += 1

    if heart_rate > 100 or heart_rate < 50:
        risk_score += 2
    if blood_sugar > 200 or blood_sugar < 70:
        risk_score += 2
    if temperature > 101.5 or temperature < 96.0:
        risk_score += 2

    try:
        systolic = int(bp.split("/")[0])
        if systolic > 160 or systolic < 90:
            risk_score += 3
        elif systolic > 140:
            risk_score += 1
    except (ValueError, IndexError):
        risk_score += 1

    if risk_score >= 7:
        return "Critical"
    elif risk_score >= 4:
        return "High"
    elif risk_score >= 2:
        return "Moderate"
    return "Low"


async def analyze_patient(
    age: int,
    gender: str,
    bp: str,
    heart_rate: int,
    blood_sugar: float,
    temperature: float,
    symptoms: List[str],
    history: List[str],
) -> Dict:
    """Simulate DRL-based clinical analysis with realistic delay."""
    logger.info(f"Analyzing patient: age={age}, gender={gender}, symptoms={symptoms}")
    await asyncio.sleep(2)

    category = _determine_category(symptoms, history)
    data = CONDITION_MAP[category]
    condition = random.choice(data["conditions"])
    risk_level = _calculate_risk(age, heart_rate, blood_sugar, bp, temperature)

    risk_confidence_map = {"Critical": 0.91, "High": 0.87, "Moderate": 0.82, "Low": 0.78}
    base_confidence = risk_confidence_map.get(risk_level, 0.80)
    confidence = round(base_confidence + random.uniform(-0.03, 0.05), 4)
    confidence = min(confidence, 0.9801)

    num_treatments = random.randint(3, 5)
    treatment_plan = random.sample(data["treatments"], min(num_treatments, len(data["treatments"])))
    num_tests = random.randint(3, 5)
    suggested_tests = random.sample(data["tests"], min(num_tests, len(data["tests"])))

    return {
        "condition": condition,
        "confidence": confidence,
        "treatment_plan": treatment_plan,
        "risk_level": risk_level,
        "suggested_tests": suggested_tests,
    }
