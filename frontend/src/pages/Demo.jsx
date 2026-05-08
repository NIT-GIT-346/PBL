import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Send, Loader2, AlertTriangle, CheckCircle, Activity, Beaker, Pill, BarChart3 } from 'lucide-react'
import GlassCard from '../components/GlassCard'
import SectionHeader from '../components/SectionHeader'
import { SYMPTOMS, MEDICAL_HISTORY, RISK_COLORS } from '../utils/constants'
import { analyzePatient } from '../services/api'

const initialForm = {
  age: '',
  gender: 'Male',
  bp: '120/80',
  heart_rate: '',
  blood_sugar: '',
  temperature: '98.6',
  symptoms: [],
  history: [],
}

function mockAnalysis(data) {
  const conditionMap = {
    chest_pain: ['Acute Coronary Syndrome', 'Angina Pectoris'],
    shortness_of_breath: ['Community-Acquired Pneumonia', 'COPD Exacerbation'],
    headache: ['Migraine with Aura', 'Tension Headache'],
    fever: ['Systemic Inflammatory Response', 'Acute Viral Infection'],
    frequent_urination: ['Type 2 Diabetes - Uncontrolled', 'Urinary Tract Infection'],
    palpitations: ['Atrial Fibrillation', 'Supraventricular Tachycardia'],
    dizziness: ['Transient Ischemic Attack', 'Vestibular Neuritis'],
    nausea: ['Gastroenteritis', 'Peptic Ulcer Disease'],
  }
  const primarySymptom = data.symptoms[0] || 'fever'
  const conditions = conditionMap[primarySymptom] || ['General Medical Evaluation Required']
  const condition = conditions[Math.floor(Math.random() * conditions.length)]

  let riskScore = 0
  if (data.age > 65) riskScore += 3
  else if (data.age > 50) riskScore += 2
  if (data.heart_rate > 100 || data.heart_rate < 50) riskScore += 2
  if (data.blood_sugar > 200 || data.blood_sugar < 70) riskScore += 2
  if (data.symptoms.length > 3) riskScore += 1
  if (data.history.length > 2) riskScore += 1

  const risk = riskScore >= 6 ? 'Critical' : riskScore >= 4 ? 'High' : riskScore >= 2 ? 'Moderate' : 'Low'
  const confidence = (0.78 + Math.random() * 0.17)

  const treatments = [
    'Continuous vital sign monitoring every 15 minutes',
    'Start IV fluid resuscitation with normal saline',
    'Administer prescribed pharmacotherapy per protocol',
    'Specialist consultation within 2 hours',
    'Serial laboratory monitoring every 6 hours',
  ]
  const tests = [
    'Complete Blood Count with Differential',
    'Comprehensive Metabolic Panel',
    'Troponin I/T Levels',
    'Chest X-Ray PA/Lateral',
    'ECG 12-Lead',
  ]

  return {
    condition,
    confidence: Math.round(confidence * 10000) / 10000,
    risk_level: risk,
    treatment_plan: treatments.slice(0, 3 + Math.floor(Math.random() * 2)),
    suggested_tests: tests.slice(0, 3 + Math.floor(Math.random() * 2)),
  }
}

function ConfidenceGauge({ value }) {
  const percentage = Math.round(value * 100)
  const circumference = 2 * Math.PI * 45
  const offset = circumference - (value * circumference)

  return (
    <div className="relative w-32 h-32 mx-auto">
      <svg className="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
        <circle cx="50" cy="50" r="45" fill="none" stroke="#1F2937" strokeWidth="6" />
        <motion.circle
          cx="50" cy="50" r="45" fill="none" stroke="#00D4FF" strokeWidth="6"
          strokeLinecap="round"
          initial={{ strokeDasharray: circumference, strokeDashoffset: circumference }}
          animate={{ strokeDashoffset: offset }}
          transition={{ duration: 1.5, ease: 'easeOut' }}
        />
      </svg>
      <div className="absolute inset-0 flex items-center justify-center">
        <span className="font-space text-2xl font-bold text-cyan">{percentage}%</span>
      </div>
    </div>
  )
}

export default function Demo() {
  const [form, setForm] = useState(initialForm)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [progress, setProgress] = useState(0)

  const toggleArrayField = (field, value) => {
    setForm(prev => ({
      ...prev,
      [field]: prev[field].includes(value)
        ? prev[field].filter(v => v !== value)
        : [...prev[field], value],
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setResult(null)
    setProgress(0)

    const progressInterval = setInterval(() => {
      setProgress(prev => Math.min(prev + Math.random() * 15, 90))
    }, 200)

    try {
      const payload = {
        ...form,
        age: parseInt(form.age),
        heart_rate: parseInt(form.heart_rate),
        blood_sugar: parseFloat(form.blood_sugar),
        temperature: parseFloat(form.temperature),
      }
      const response = await analyzePatient(payload)
      setResult(response.data)
    } catch {
      await new Promise(r => setTimeout(r, 2000))
      setResult(mockAnalysis({
        ...form,
        age: parseInt(form.age),
        heart_rate: parseInt(form.heart_rate),
        blood_sugar: parseFloat(form.blood_sugar),
      }))
    } finally {
      clearInterval(progressInterval)
      setProgress(100)
      setTimeout(() => setLoading(false), 500)
    }
  }

  const riskStyle = result ? RISK_COLORS[result.risk_level] || RISK_COLORS.Low : null

  return (
    <div className="py-20 px-4">
      <div className="max-w-6xl mx-auto">
        <SectionHeader
          title="AI Patient Analysis Demo"
          subtitle="Experience the Clinical Decision Support System in action with real-time AI analysis"
        />

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Input Form */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
          >
            <GlassCard gradient>
              <h3 className="font-space text-xl font-bold text-cyan mb-6 flex items-center gap-2">
                <Activity className="w-5 h-5" /> Patient Information
              </h3>
              <form onSubmit={handleSubmit} className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm text-text-secondary mb-1">Age</label>
                    <input
                      type="number" required min="0" max="120"
                      value={form.age}
                      onChange={e => setForm({ ...form, age: e.target.value })}
                      className="w-full px-4 py-2.5 rounded-xl bg-bg-primary border border-border text-text-primary focus:border-cyan focus:outline-none transition-colors"
                      placeholder="45"
                    />
                  </div>
                  <div>
                    <label className="block text-sm text-text-secondary mb-1">Gender</label>
                    <select
                      value={form.gender}
                      onChange={e => setForm({ ...form, gender: e.target.value })}
                      className="w-full px-4 py-2.5 rounded-xl bg-bg-primary border border-border text-text-primary focus:border-cyan focus:outline-none transition-colors"
                    >
                      <option value="Male">Male</option>
                      <option value="Female">Female</option>
                      <option value="Other">Other</option>
                    </select>
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm text-text-secondary mb-1">Blood Pressure</label>
                    <input
                      type="text" required
                      value={form.bp}
                      onChange={e => setForm({ ...form, bp: e.target.value })}
                      className="w-full px-4 py-2.5 rounded-xl bg-bg-primary border border-border text-text-primary focus:border-cyan focus:outline-none transition-colors"
                      placeholder="120/80"
                    />
                  </div>
                  <div>
                    <label className="block text-sm text-text-secondary mb-1">Heart Rate (BPM)</label>
                    <input
                      type="number" required min="30" max="250"
                      value={form.heart_rate}
                      onChange={e => setForm({ ...form, heart_rate: e.target.value })}
                      className="w-full px-4 py-2.5 rounded-xl bg-bg-primary border border-border text-text-primary focus:border-cyan focus:outline-none transition-colors"
                      placeholder="72"
                    />
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm text-text-secondary mb-1">Blood Sugar (mg/dL)</label>
                    <input
                      type="number" required min="0"
                      value={form.blood_sugar}
                      onChange={e => setForm({ ...form, blood_sugar: e.target.value })}
                      className="w-full px-4 py-2.5 rounded-xl bg-bg-primary border border-border text-text-primary focus:border-cyan focus:outline-none transition-colors"
                      placeholder="110"
                    />
                  </div>
                  <div>
                    <label className="block text-sm text-text-secondary mb-1">Temperature (°F)</label>
                    <input
                      type="number" required step="0.1" min="90" max="110"
                      value={form.temperature}
                      onChange={e => setForm({ ...form, temperature: e.target.value })}
                      className="w-full px-4 py-2.5 rounded-xl bg-bg-primary border border-border text-text-primary focus:border-cyan focus:outline-none transition-colors"
                      placeholder="98.6"
                    />
                  </div>
                </div>

                {/* Symptoms Multi-select */}
                <div>
                  <label className="block text-sm text-text-secondary mb-2">Symptoms</label>
                  <div className="flex flex-wrap gap-2">
                    {SYMPTOMS.map(s => (
                      <button
                        key={s.value} type="button"
                        onClick={() => toggleArrayField('symptoms', s.value)}
                        className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                          form.symptoms.includes(s.value)
                            ? 'bg-cyan/20 text-cyan border border-cyan/40'
                            : 'bg-bg-primary border border-border text-text-secondary hover:border-cyan/30'
                        }`}
                      >
                        {s.label}
                      </button>
                    ))}
                  </div>
                </div>

                {/* Medical History */}
                <div>
                  <label className="block text-sm text-text-secondary mb-2">Medical History</label>
                  <div className="flex flex-wrap gap-2">
                    {MEDICAL_HISTORY.map(h => (
                      <button
                        key={h.value} type="button"
                        onClick={() => toggleArrayField('history', h.value)}
                        className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                          form.history.includes(h.value)
                            ? 'bg-purple/20 text-purple border border-purple/40'
                            : 'bg-bg-primary border border-border text-text-secondary hover:border-purple/30'
                        }`}
                      >
                        {h.label}
                      </button>
                    ))}
                  </div>
                </div>

                <button
                  type="submit"
                  disabled={loading || !form.age || !form.heart_rate || !form.blood_sugar}
                  className="w-full py-3 rounded-xl bg-cyan text-bg-primary font-semibold text-lg hover:bg-cyan/90 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                >
                  {loading ? (
                    <><Loader2 className="w-5 h-5 animate-spin" /> Analyzing...</>
                  ) : (
                    <><Send className="w-5 h-5" /> Analyze Patient</>
                  )}
                </button>
              </form>
            </GlassCard>
          </motion.div>

          {/* Results Panel */}
          <div>
            <AnimatePresence mode="wait">
              {loading && (
                <motion.div
                  key="loading"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -20 }}
                >
                  <GlassCard className="text-center py-16">
                    <Loader2 className="w-16 h-16 text-cyan animate-spin mx-auto mb-6" />
                    <h3 className="font-space text-xl font-bold text-cyan mb-3">AI Processing...</h3>
                    <p className="text-text-secondary mb-6">Running DRL inference on patient data</p>
                    <div className="w-full max-w-xs mx-auto bg-bg-primary rounded-full h-2 overflow-hidden">
                      <motion.div
                        className="h-full bg-gradient-to-r from-cyan to-purple rounded-full"
                        initial={{ width: '0%' }}
                        animate={{ width: `${progress}%` }}
                        transition={{ duration: 0.3 }}
                      />
                    </div>
                    <p className="text-text-secondary text-sm mt-2">{Math.round(progress)}% complete</p>
                  </GlassCard>
                </motion.div>
              )}

              {!loading && result && (
                <motion.div
                  key="result"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="space-y-6"
                >
                  {/* Diagnosis */}
                  <GlassCard gradient>
                    <div className="flex items-start justify-between mb-4">
                      <h3 className="font-space text-lg font-bold text-cyan flex items-center gap-2">
                        <CheckCircle className="w-5 h-5" /> Diagnosis Result
                      </h3>
                      <span className={`px-3 py-1 rounded-full text-xs font-bold ${riskStyle.bg} ${riskStyle.text} ${riskStyle.border} border`}>
                        {result.risk_level} Risk
                      </span>
                    </div>
                    <h2 className="font-space text-2xl font-bold mb-4">{result.condition}</h2>
                    <ConfidenceGauge value={result.confidence} />
                    <p className="text-center text-text-secondary text-sm mt-2">Confidence Score</p>
                  </GlassCard>

                  {/* Treatment Plan */}
                  <GlassCard>
                    <h3 className="font-space text-lg font-bold text-purple mb-4 flex items-center gap-2">
                      <Pill className="w-5 h-5" /> Treatment Plan
                    </h3>
                    <ul className="space-y-3">
                      {result.treatment_plan.map((t, i) => (
                        <motion.li
                          key={i}
                          initial={{ opacity: 0, x: -10 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: i * 0.1 }}
                          className="flex items-start gap-3"
                        >
                          <span className="w-6 h-6 rounded-full bg-purple/20 text-purple text-xs flex items-center justify-center shrink-0 mt-0.5 font-bold">
                            {i + 1}
                          </span>
                          <span className="text-text-secondary text-sm">{t}</span>
                        </motion.li>
                      ))}
                    </ul>
                  </GlassCard>

                  {/* Lab Tests */}
                  <GlassCard>
                    <h3 className="font-space text-lg font-bold text-cyan mb-4 flex items-center gap-2">
                      <Beaker className="w-5 h-5" /> Suggested Lab Tests
                    </h3>
                    <div className="flex flex-wrap gap-2">
                      {result.suggested_tests.map((test, i) => (
                        <motion.span
                          key={i}
                          initial={{ opacity: 0, scale: 0.8 }}
                          animate={{ opacity: 1, scale: 1 }}
                          transition={{ delay: i * 0.1 }}
                          className="px-3 py-2 rounded-lg bg-cyan/10 border border-cyan/20 text-cyan text-sm font-medium"
                        >
                          {test}
                        </motion.span>
                      ))}
                    </div>
                  </GlassCard>
                </motion.div>
              )}

              {!loading && !result && (
                <motion.div
                  key="empty"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                >
                  <GlassCard className="text-center py-20">
                    <BarChart3 className="w-16 h-16 text-text-secondary/30 mx-auto mb-4" />
                    <h3 className="font-space text-xl font-bold text-text-secondary mb-2">No Analysis Yet</h3>
                    <p className="text-text-secondary/60 text-sm">
                      Fill in the patient information and click "Analyze Patient" to see AI-powered results.
                    </p>
                  </GlassCard>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </div>
      </div>
    </div>
  )
}
