import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from database.connection import init_db
from routes.patient import router as patient_router
from routes.metrics import router as metrics_router
from routes.pipeline import router as pipeline_router
from routes.auth import router as auth_router
from middleware.error_handler import add_error_handlers

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Clinical DSS API server...")
    await init_db()
    logger.info("Database initialized.")
    yield
    logger.info("Shutting down Clinical DSS API server...")


app = FastAPI(
    title="Clinical Decision Support System API",
    description="Deep Reinforcement Learning-based Clinical Decision Support System using Big Data Analytics",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_error_handlers(app)

app.include_router(auth_router, prefix="/api", tags=["Authentication"])
app.include_router(patient_router, prefix="/api", tags=["Patient Analysis"])
app.include_router(metrics_router, prefix="/api", tags=["Model Metrics"])
app.include_router(pipeline_router, prefix="/api", tags=["Pipeline"])


@app.get("/", tags=["Health"])
async def root():
    return {
        "status": "healthy",
        "service": "Clinical DSS API",
        "version": "1.0.0",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
