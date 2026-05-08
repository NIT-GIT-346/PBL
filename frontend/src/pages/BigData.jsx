import { motion } from 'framer-motion'
import { ArrowRight } from 'lucide-react'
import GlassCard from '../components/GlassCard'
import SectionHeader from '../components/SectionHeader'
import { BIG_DATA_TECHNOLOGIES } from '../data/mockData'

const stepStyles = {
  cyan: 'bg-cyan/10 border-cyan/30 text-cyan',
  purple: 'bg-purple/10 border-purple/30 text-purple',
}

const flowSteps = [
  { label: 'EHR Data', color: 'cyan' },
  { label: 'Kafka Ingest', color: 'purple' },
  { label: 'HDFS Storage', color: 'cyan' },
  { label: 'Spark Process', color: 'purple' },
  { label: 'Feature Store', color: 'cyan' },
  { label: 'DRL Engine', color: 'purple' },
]

export default function BigData() {
  return (
    <div className="py-20 px-4">
      <div className="max-w-6xl mx-auto">
        <SectionHeader
          title="Big Data Pipeline"
          subtitle="Distributed computing infrastructure powering real-time clinical analytics"
        />

        {/* Animated Data Flow */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-16"
        >
          <GlassCard className="overflow-x-auto">
            <h3 className="font-space text-lg font-bold text-center mb-6">Data Flow Visualization</h3>
            <div className="flex items-center justify-center gap-2 min-w-max px-4">
              {flowSteps.map((step, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, x: -20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: i * 0.15 }}
                  className="flex items-center gap-2"
                >
                  <div className={`px-4 py-3 rounded-xl border ${stepStyles[step.color]} font-medium text-sm whitespace-nowrap`}>
                    {step.label}
                  </div>
                  {i < flowSteps.length - 1 && (
                    <motion.div
                      animate={{ x: [0, 5, 0] }}
                      transition={{ repeat: Infinity, duration: 1.5, delay: i * 0.2 }}
                    >
                      <ArrowRight className="w-4 h-4 text-text-secondary" />
                    </motion.div>
                  )}
                </motion.div>
              ))}
            </div>
          </GlassCard>
        </motion.div>

        {/* Technology Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {BIG_DATA_TECHNOLOGIES.map((tech, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
            >
              <GlassCard className="h-full" gradient>
                <div className="text-4xl mb-3">{tech.icon}</div>
                <h3 className="font-space text-lg font-bold text-cyan mb-2">{tech.name}</h3>
                <p className="text-text-secondary text-sm mb-4 leading-relaxed">{tech.description}</p>

                <div className="mb-4">
                  <div className="text-xs font-bold text-purple mb-2 uppercase tracking-wider">Features</div>
                  <ul className="space-y-1.5">
                    {tech.features.map((f, j) => (
                      <li key={j} className="flex items-center gap-2 text-sm text-text-secondary">
                        <div className="w-1.5 h-1.5 rounded-full bg-cyan" />
                        {f}
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="pt-4 border-t border-border/50">
                  <div className="text-xs font-bold text-purple mb-2 uppercase tracking-wider">Metrics</div>
                  <div className="grid grid-cols-2 gap-2">
                    {Object.entries(tech.metrics).map(([key, value]) => (
                      <div key={key} className="text-sm">
                        <span className="text-text-secondary">{key}: </span>
                        <span className="text-cyan font-medium">{value}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </GlassCard>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  )
}
