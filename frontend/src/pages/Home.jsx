import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { ArrowRight, Activity, Brain, Database, Shield } from 'lucide-react'
import NeuralBackground from '../components/NeuralBackground'
import StatCounter from '../components/StatCounter'
import GlassCard from '../components/GlassCard'
import SectionHeader from '../components/SectionHeader'
import { STATS, HOW_IT_WORKS } from '../data/mockData'

const stepIcons = [Database, Activity, Brain, Shield]

export default function Home() {
  return (
    <div>
      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
        <NeuralBackground />
        <div className="relative z-10 max-w-5xl mx-auto px-4 text-center">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-cyan/10 border border-cyan/20 text-cyan text-sm mb-8">
              <Activity className="w-4 h-4" />
              AI-Powered Clinical Decision Support
            </div>
            <h1 className="font-space text-4xl sm:text-5xl md:text-7xl font-bold leading-tight mb-6">
              Deep Reinforcement Learning{' '}
              <span className="text-cyan text-glow-cyan">Clinical DSS</span>
            </h1>
            <p className="text-text-secondary text-lg sm:text-xl max-w-3xl mx-auto mb-10 leading-relaxed">
              Leveraging Big Data Analytics and Deep Reinforcement Learning to transform
              clinical decision-making with intelligent, real-time patient analysis.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                to="/demo"
                className="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-xl bg-cyan text-bg-primary font-semibold text-lg hover:bg-cyan/90 transition-all glow-cyan"
              >
                Try Live Demo <ArrowRight className="w-5 h-5" />
              </Link>
              <Link
                to="/about"
                className="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-xl border border-purple/50 text-purple font-semibold text-lg hover:bg-purple/10 transition-all"
              >
                Learn More
              </Link>
            </div>
          </motion.div>
        </div>
        <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-bg-primary to-transparent" />
      </section>

      {/* Stats Section */}
      <section className="py-20 px-4">
        <div className="max-w-5xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8">
          {STATS.map((stat, i) => (
            <StatCounter key={i} label={stat.label} value={stat.value} suffix={stat.suffix} />
          ))}
        </div>
      </section>

      {/* How It Works */}
      <section className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          <SectionHeader title="How It Works" subtitle="Our four-step pipeline transforms raw clinical data into actionable insights" />
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {HOW_IT_WORKS.map((item, i) => {
              const Icon = stepIcons[i]
              return (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, y: 30 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: i * 0.15 }}
                >
                  <GlassCard className="h-full text-center">
                    <div className="w-16 h-16 rounded-2xl bg-cyan/10 flex items-center justify-center mx-auto mb-4">
                      <Icon className="w-8 h-8 text-cyan" />
                    </div>
                    <div className="text-xs font-bold text-purple mb-2">STEP {item.step}</div>
                    <h3 className="font-space font-semibold text-lg mb-3">{item.title}</h3>
                    <p className="text-text-secondary text-sm leading-relaxed">{item.description}</p>
                  </GlassCard>
                </motion.div>
              )
            })}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 px-4">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="max-w-4xl mx-auto text-center glass-card p-12 gradient-border"
        >
          <h2 className="font-space text-3xl font-bold mb-4">Ready to Explore?</h2>
          <p className="text-text-secondary mb-8 text-lg">
            Experience the power of Deep Reinforcement Learning in clinical decision-making.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              to="/demo"
              className="inline-flex items-center justify-center gap-2 px-8 py-3 rounded-xl bg-cyan text-bg-primary font-semibold hover:bg-cyan/90 transition-all"
            >
              Launch Demo <ArrowRight className="w-5 h-5" />
            </Link>
            <Link
              to="/architecture"
              className="inline-flex items-center justify-center gap-2 px-8 py-3 rounded-xl border border-border text-text-primary font-semibold hover:bg-white/5 transition-all"
            >
              View Architecture
            </Link>
          </div>
        </motion.div>
      </section>
    </div>
  )
}
