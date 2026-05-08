import { motion } from 'framer-motion'
import {
  LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, Legend,
} from 'recharts'
import { TrendingUp, Award, Target, Zap } from 'lucide-react'
import GlassCard from '../components/GlassCard'
import SectionHeader from '../components/SectionHeader'
import { DRL_TRAINING_DATA, MODEL_COMPARISON, CONFUSION_MATRIX } from '../data/mockData'

const colorStyles = {
  cyan: { icon: 'text-cyan', text: 'text-cyan' },
  purple: { icon: 'text-purple', text: 'text-purple' },
}

const metricCards = [
  { icon: TrendingUp, label: 'Best Accuracy', value: '94.23%', color: 'cyan' },
  { icon: Award, label: 'F1 Score', value: '93.49%', color: 'purple' },
  { icon: Target, label: 'AUC-ROC', value: '96.78%', color: 'cyan' },
  { icon: Zap, label: 'Inference Time', value: '85ms', color: 'purple' },
]

const CustomTooltip = ({ active, payload, label }) => {
  if (!active || !payload) return null
  return (
    <div className="glass-card p-3 text-sm" style={{ borderRadius: '0.5rem' }}>
      <p className="text-text-secondary mb-1">{label}</p>
      {payload.map((entry, i) => (
        <p key={i} style={{ color: entry.color }} className="font-medium">
          {entry.name}: {typeof entry.value === 'number' ? entry.value.toFixed(2) : entry.value}
        </p>
      ))}
    </div>
  )
}

function HeatmapCell({ value, maxVal }) {
  const intensity = value / maxVal
  const isDiagonal = intensity > 0.7
  const bg = isDiagonal
    ? `rgba(0, 212, 255, ${0.3 + intensity * 0.5})`
    : `rgba(124, 58, 237, ${intensity * 0.4})`

  return (
    <div
      className="w-full aspect-square flex items-center justify-center rounded-md text-xs font-bold transition-all hover:scale-105"
      style={{ backgroundColor: bg }}
    >
      {value}
    </div>
  )
}

export default function Results() {
  const maxVal = Math.max(...CONFUSION_MATRIX.matrix.flat())

  return (
    <div className="py-20 px-4">
      <div className="max-w-6xl mx-auto">
        <SectionHeader
          title="Research Results"
          subtitle="Comprehensive evaluation metrics and performance analysis of the DRL-based CDSS"
        />

        {/* Metric Cards */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
          {metricCards.map((card, i) => {
            const Icon = card.icon
            return (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
              >
                <GlassCard className="text-center">
                  <Icon className={`w-8 h-8 ${colorStyles[card.color].icon} mx-auto mb-2`} />
                  <div className={`font-space text-2xl font-bold ${colorStyles[card.color].text} mb-1`}>{card.value}</div>
                  <div className="text-text-secondary text-xs">{card.label}</div>
                </GlassCard>
              </motion.div>
            )
          })}
        </div>

        {/* DRL Training Chart */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <GlassCard>
            <h3 className="font-space text-xl font-bold text-cyan mb-6">DRL Training Progress</h3>
            <ResponsiveContainer width="100%" height={350}>
              <LineChart data={DRL_TRAINING_DATA}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
                <XAxis dataKey="episode" stroke="#9CA3AF" tick={{ fontSize: 11 }} />
                <YAxis yAxisId="left" stroke="#00D4FF" tick={{ fontSize: 11 }} />
                <YAxis yAxisId="right" orientation="right" stroke="#7C3AED" tick={{ fontSize: 11 }} />
                <Tooltip content={<CustomTooltip />} />
                <Legend wrapperStyle={{ color: '#9CA3AF', fontSize: 12 }} />
                <Line yAxisId="left" type="monotone" dataKey="reward" stroke="#00D4FF" strokeWidth={2} dot={false} name="Reward" />
                <Line yAxisId="right" type="monotone" dataKey="accuracy" stroke="#7C3AED" strokeWidth={2} dot={false} name="Accuracy" />
              </LineChart>
            </ResponsiveContainer>
          </GlassCard>
        </motion.div>

        {/* Model Comparison */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <GlassCard>
            <h3 className="font-space text-xl font-bold text-purple mb-6">Model Comparison</h3>
            <ResponsiveContainer width="100%" height={350}>
              <BarChart data={MODEL_COMPARISON} layout="vertical">
                <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
                <XAxis type="number" domain={[70, 100]} stroke="#9CA3AF" tick={{ fontSize: 11 }} />
                <YAxis type="category" dataKey="model" stroke="#9CA3AF" tick={{ fontSize: 11 }} width={110} />
                <Tooltip content={<CustomTooltip />} />
                <Legend wrapperStyle={{ color: '#9CA3AF', fontSize: 12 }} />
                <Bar dataKey="accuracy" fill="#00D4FF" name="Accuracy %" radius={[0, 4, 4, 0]} />
                <Bar dataKey="f1" fill="#7C3AED" name="F1 Score %" radius={[0, 4, 4, 0]} />
                <Bar dataKey="auc" fill="#10B981" name="AUC-ROC %" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </GlassCard>
        </motion.div>

        {/* Confusion Matrix */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <GlassCard>
            <h3 className="font-space text-xl font-bold text-cyan mb-6">Confusion Matrix Heatmap</h3>
            <div className="overflow-x-auto">
              <div className="min-w-[400px]">
                <div className="grid gap-1" style={{ gridTemplateColumns: `80px repeat(${CONFUSION_MATRIX.labels.length}, 1fr)` }}>
                  <div />
                  {CONFUSION_MATRIX.labels.map((label, i) => (
                    <div key={i} className="text-center text-xs text-text-secondary font-medium py-2 truncate px-1">
                      {label}
                    </div>
                  ))}
                  {CONFUSION_MATRIX.matrix.map((row, i) => (
                    <div key={i} className="contents">
                      <div className="flex items-center text-xs text-text-secondary font-medium pr-2 truncate">
                        {CONFUSION_MATRIX.labels[i]}
                      </div>
                      {row.map((val, j) => (
                        <HeatmapCell key={j} value={val} maxVal={maxVal} />
                      ))}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </GlassCard>
        </motion.div>

        {/* Dataset Info */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
        >
          <GlassCard gradient>
            <h3 className="font-space text-xl font-bold text-purple mb-4">Dataset Information</h3>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
              {[
                { label: 'Total Records', value: '52,847' },
                { label: 'Training Set', value: '37,993 (72%)' },
                { label: 'Validation Set', value: '7,898 (15%)' },
                { label: 'Test Set', value: '6,956 (13%)' },
                { label: 'Features', value: '148' },
                { label: 'Target Classes', value: '5' },
                { label: 'Training Epochs', value: '1,000' },
                { label: 'Batch Size', value: '32' },
              ].map((item, i) => (
                <div key={i}>
                  <div className="text-text-secondary text-xs mb-1">{item.label}</div>
                  <div className="font-space font-bold text-lg text-cyan">{item.value}</div>
                </div>
              ))}
            </div>
          </GlassCard>
        </motion.div>
      </div>
    </div>
  )
}
