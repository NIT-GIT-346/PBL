import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE,
  headers: { 'Content-Type': 'application/json' },
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('cdss_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export const analyzePatient = (data) => api.post('/api/analyze-patient', data)
export const getModelMetrics = () => api.get('/api/model-metrics')
export const getPipelineStatus = () => api.get('/api/pipeline-status')
export const getRecentCases = () => api.get('/api/recent-cases')
export const login = (credentials) => api.post('/api/auth/token', credentials)

export default api
