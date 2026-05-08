import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime, JSON
from database.connection import Base


class PatientCase(Base):
    __tablename__ = "patient_cases"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    bp = Column(String, nullable=False)
    heart_rate = Column(Integer, nullable=False)
    blood_sugar = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    symptoms = Column(JSON, nullable=False)
    history = Column(JSON, nullable=False)
    condition = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    risk_level = Column(String, nullable=False)
    treatment_plan = Column(JSON, nullable=False)
    suggested_tests = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
