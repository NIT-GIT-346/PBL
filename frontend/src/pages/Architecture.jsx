import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ChevronDown, ChevronUp } from 'lucide-react'
import GlassCard from '../components/GlassCard'
import SectionHeader from '../components/SectionHeader'
import { ARCHITECTURE_NODES } from '../data/mockData'

export default function Architecture() {
  const [expandedNode, setExpandedNode] = useState(null)

  return (
    <div className="py-20 px-4">
      <div className="max-w-5xl mx-auto">
        <SectionHeader
          title="System Architecture"
          subtitle="Interactive overview of the Clinical DSS data flow pipeline"
        />

        <div className="relative">
          {/* Connection line */}
          <div className="absolute left-1/2 top-0 bottom-0 w-0.5 bg-gradient-to-b from-cyan via-purple to-cyan hidden md:block" style={{ transform: 'translateX(-50%)' }} />

          <div className="space-y-6">
            {ARCHITECTURE_NODES.map((node, i) => {
              const isExpanded = expandedNode === node.id
              const colorClass = node.color === 'cyan' ? 'text-cyan' : 'text-purple'
              const bgClass = node.color === 'cyan' ? 'bg-cyan/10' : 'bg-purple/10'
              const borderClass = node.color === 'cyan' ? 'border-cyan/30' : 'border-purple/30'

              return (
                <motion.div
                  key={node.id}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: i * 0.1 }}
                  className="relative"
                >
                  {/* Connector dot */}
                  <div className={`absolute left-1/2 top-8 w-4 h-4 rounded-full ${bgClass} border-2 ${borderClass} transform -translate-x-1/2 z-10 hidden md:block`} />

                  <div
                    onClick={() => setExpandedNode(isExpanded ? null : node.id)}
                    className={`glass-card p-6 cursor-pointer transition-all duration-300 hover:border-${node.color}/30 ${isExpanded ? `border-${node.color}/40` : ''}`}
                    style={{ borderRadius: '1rem' }}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-4">
                        <div className={`w-12 h-12 rounded-xl ${bgClass} flex items-center justify-center`}>
                          <span className="text-2xl font-bold font-space">{i + 1}</span>
                        </div>
                        <div>
                          <h3 className={`font-space text-xl font-bold ${colorClass}`}>{node.title}</h3>
                          <p className="text-text-secondary text-sm mt-1">{node.description}</p>
                        </div>
                      </div>
                      <div className={`${colorClass}`}>
                        {isExpanded ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
                      </div>
                    </div>

                    <AnimatePresence>
                      {isExpanded && (
                        <motion.div
                          initial={{ opacity: 0, height: 0 }}
                          animate={{ opacity: 1, height: 'auto' }}
                          exit={{ opacity: 0, height: 0 }}
                          transition={{ duration: 0.3 }}
                          className="overflow-hidden"
                        >
                          <div className={`mt-4 pt-4 border-t border-border/50`}>
                            <p className="text-text-secondary leading-relaxed">{node.details}</p>
                          </div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>

                  {/* Arrow between nodes */}
                  {i < ARCHITECTURE_NODES.length - 1 && (
                    <div className="flex justify-center my-2 md:hidden">
                      <div className="w-0.5 h-6 bg-gradient-to-b from-cyan/50 to-purple/50" />
                    </div>
                  )}
                </motion.div>
              )
            })}
          </div>
        </div>

        {/* Flow Summary */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mt-16"
        >
          <GlassCard gradient className="text-center">
            <h3 className="font-space text-xl font-bold text-cyan mb-3">End-to-End Pipeline</h3>
            <div className="flex flex-wrap items-center justify-center gap-3 text-sm">
              {['Data Sources', 'Big Data Layer', 'DRL Engine', 'CDSS Module', 'Clinical Output'].map((step, i) => (
                <span key={i} className="flex items-center gap-3">
                  <span className="px-3 py-1.5 rounded-lg bg-cyan/10 text-cyan font-medium">{step}</span>
                  {i < 4 && <span className="text-purple font-bold">→</span>}
                </span>
              ))}
            </div>
          </GlassCard>
        </motion.div>
      </div>
    </div>
  )
}
