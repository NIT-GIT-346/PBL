from pydantic import BaseModel, Field
from typing import List, Optional


class PatientInput(BaseModel):
    age: int = Field(..., ge=0, le=120, description="Patient age")
    gender: str = Field(..., description="Patient gender")
    bp: str = Field(..., description="Blood pressure reading (e.g., '120/80')")
    heart_rate: int = Field(..., ge=30, le=250, description="Heart rate in BPM")
    blood_sugar: float = Field(..., ge=0, description="Blood sugar level mg/dL")
    temperature: float = Field(..., ge=90, le=110, description="Body temperature in °F")
    symptoms: List[str] = Field(default_factory=list, description="List of symptoms")
    history: List[str] = Field(default_factory=list, description="Medical history")


class DiagnosisOutput(BaseModel):
    condition: str
    confidence: float
    treatment_plan: List[str]
    risk_level: str
    suggested_tests: List[str]


class PatientCaseResponse(BaseModel):
    id: str
    age: int
    gender: str
    condition: str
    confidence: float
    risk_level: str
    created_at: str


class ModelMetrics(BaseModel):
    model_name: str
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    auc_roc: float


class PipelineStatus(BaseModel):
    component: str
    status: str
    throughput: str
    latency: str
    last_updated: str
