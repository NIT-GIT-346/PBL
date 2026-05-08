import { motion } from 'framer-motion'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import GlassCard from '../components/GlassCard'
import SectionHeader from '../components/SectionHeader'
import { DRL_CONCEPTS, DRL_TRAINING_DATA } from '../data/mockData'

export default function DRL() {
  return (
    <div className="py-20 px-4">
      <div className="max-w-6xl mx-auto">
        <SectionHeader
          title="Deep Reinforcement Learning"
          subtitle="Understanding the AI engine that powers clinical decision-making"
          accent="purple"
        />

        {/* DRL Components */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 mb-16">
          {DRL_CONCEPTS.components.map((comp, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
            >
              <GlassCard className="text-center h-full">
                <div className="text-3xl mb-3">{comp.icon}</div>
                <h4 className="font-space font-bold text-cyan mb-2">{comp.name}</h4>
                <p className="text-text-secondary text-xs leading-relaxed">{comp.description}</p>
              </GlassCard>
            </motion.div>
          ))}
        </div>

        {/* Algorithm Cards */}
        <SectionHeader title="DRL Algorithms" subtitle="Advanced algorithms optimized for clinical decision tasks" />
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-16">
          {DRL_CONCEPTS.algorithms.map((algo, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.15 }}
            >
              <GlassCard className="h-full" gradient>
                <h3 className="font-space text-lg font-bold text-purple mb-2">{algo.name}</h3>
                <p className="text-text-secondary text-sm mb-4 leading-relaxed">{algo.description}</p>
                <div className="mb-4">
                  {algo.features.map((f, j) => (
                    <span key={j} className="inline-block px-2 py-1 rounded-md bg-purple/10 text-purple text-xs font-medium mr-2 mb-2">
                      {f}
                    </span>
                  ))}
                </div>
                <div className="pt-3 border-t border-border/50 flex items-center justify-between">
                  <span className="text-text-secondary text-sm">Accuracy</span>
                  <span className="text-cyan font-space font-bold text-lg">{algo.accuracy}%</span>
                </div>
              </GlassCard>
            </motion.div>
          ))}
        </div>

        {/* Reward Chart */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-16"
        >
          <GlassCard>
            <h3 className="font-space text-xl font-bold text-cyan mb-6">DRL Training Progress — Reward Over Episodes</h3>
            <ResponsiveContainer width="100%" height={400}>
              <LineChart data={DRL_TRAINING_DATA}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" />
                <XAxis dataKey="episode" stroke="#9CA3AF" tick={{ fontSize: 12 }} label={{ value: 'Episode', position: 'insideBottom', offset: -5, fill: '#9CA3AF' }} />
                <YAxis stroke="#9CA3AF" tick={{ fontSize: 12 }} label={{ value: 'Reward', angle: -90, position: 'insideLeft', fill: '#9CA3AF' }} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#111827', border: '1px solid #1F2937', borderRadius: '0.5rem', color: '#F3F4F6' }}
                  labelStyle={{ color: '#9CA3AF' }}
                />
                <Line type="monotone" dataKey="reward" stroke="#00D4FF" strokeWidth={2} dot={false} />
              </LineChart>
            </ResponsiveContainer>
          </GlassCard>
        </motion.div>

        {/* Pseudocode */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
        >
          <GlassCard>
            <h3 className="font-space text-xl font-bold text-purple mb-4">DQN Algorithm — Pseudocode</h3>
            <div className="rounded-xl bg-bg-primary p-6 overflow-x-auto">
              <pre className="text-sm font-mono leading-relaxed">
                <code className="text-cyan/80 whitespace-pre">{DRL_CONCEPTS.pseudocode}</code>
              </pre>
            </div>
          </GlassCard>
        </motion.div>
      </div>
    </div>
  )
}
