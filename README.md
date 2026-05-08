# Deep Reinforcement Learning-based Clinical Decision Support System

A full-stack research web application demonstrating a Clinical Decision Support System (CDSS) powered by Deep Reinforcement Learning and Big Data Analytics.

## Tech Stack

### Frontend
- **React.js + Vite** — Fast development and optimized builds
- **React Router DOM** — Client-side routing with animated transitions
- **Tailwind CSS** — Utility-first styling with custom dark theme
- **Framer Motion** — Smooth page transitions and animations
- **Recharts** — Interactive charts and data visualizations
- **Axios** — HTTP client for API communication
- **Lucide React** — Modern icon library

### Backend
- **Python FastAPI** — High-performance async API framework
- **PostgreSQL** — Primary database for patient case storage
- **Redis** — Caching layer for improved performance
- **JWT Authentication** — Secure token-based auth
- **Simulated Kafka** — Mock streaming data pipeline
- **Uvicorn** — ASGI server

### DevOps
- **Docker + Docker Compose** — Containerized deployment
- **Nginx** — Frontend reverse proxy with API passthrough

## Project Structure

```
root/
├── frontend/               # React + Vite frontend
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page components (Home, Demo, Results, etc.)
│   │   ├── layouts/        # Layout wrappers
│   │   ├── hooks/          # Custom React hooks
│   │   ├── services/       # API service layer
│   │   ├── context/        # React context (Theme)
│   │   ├── data/           # Mock data and constants
│   │   ├── styles/         # Global CSS with Tailwind
│   │   └── utils/          # Utility functions
│   ├── Dockerfile
│   └── nginx.conf
├── backend/                # FastAPI backend
│   ├── routes/             # API route handlers
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   ├── services/           # Business logic (AI engine, cache, Kafka sim)
│   ├── database/           # Database connection and setup
│   ├── middleware/         # Error handling middleware
│   ├── mock_data/          # Realistic mock medical data
│   ├── utils/              # Auth utilities
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── .env.example
└── README.md
```

## Pages

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Hero section with neural background, stats, how-it-works |
| About | `/about` | Problem statement, objectives, three pillars, timeline |
| Architecture | `/architecture` | Interactive expandable system architecture diagram |
| Big Data | `/big-data` | Data pipeline visualization with technology cards |
| DRL | `/drl` | DRL concepts, algorithms, training chart, pseudocode |
| Demo | `/demo` | **AI patient analysis simulator** with real-time results |
| Results | `/results` | Metric cards, training charts, confusion matrix heatmap |
| Team | `/team` | Team cards, supervisor, project timeline, references |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/analyze-patient` | Analyze patient data with AI simulation |
| GET | `/api/model-metrics` | Get model performance metrics |
| GET | `/api/pipeline-status` | Get big data pipeline status |
| GET | `/api/recent-cases` | Get recent analysis cases |
| POST | `/api/auth/token` | JWT authentication |

## Quick Start

### Using Docker (Recommended)

```bash
# Clone the repository
git clone <repo-url>
cd clinical-dss

# Start all services
docker-compose up --build

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Manual Setup

#### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
# Opens at http://localhost:5173
```

## Demo Credentials

| Username | Password | Role |
|----------|----------|------|
| admin | cdss2024 | Admin |
| researcher | research2024 | Researcher |

## Features

- **Dark Futuristic UI** — Cyberpunk medical dashboard aesthetic with glassmorphism
- **Animated Neural Background** — Canvas-based particle network on homepage
- **AI Patient Simulator** — Full patient analysis with confidence gauge and risk badges
- **Interactive Charts** — DRL training progress, model comparisons, confusion matrix
- **Responsive Design** — Mobile, tablet, and desktop optimized
- **Smooth Animations** — Framer Motion page transitions and scroll reveals
- **Theme Toggle** — Dark/light mode support
- **JWT Authentication** — Secure API access
- **Redis Caching** — Performance optimized responses
- **Mock Kafka Streaming** — Simulated real-time data pipeline

## Screenshots

> Screenshots will be added after deployment.

## License

This project is for research and educational purposes.
