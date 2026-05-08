import { motion } from 'framer-motion'
import { Database, Brain, Stethoscope, ArrowRight } from 'lucide-react'
import GlassCard from '../components/GlassCard'
import SectionHeader from '../components/SectionHeader'

const colorMap = {
  cyan: { bg: 'bg-cyan/10', text: 'text-cyan', dot: 'bg-cyan', icon: 'text-cyan' },
  purple: { bg: 'bg-purple/10', text: 'text-purple', dot: 'bg-purple', icon: 'text-purple' },
}

const pillars = [
  {
    icon: Database,
    title: 'Big Data Analytics',
    color: 'cyan',
    description: 'Processing and analyzing massive healthcare datasets using distributed computing frameworks for pattern discovery and feature extraction.',
    features: ['Apache Hadoop & Spark', 'Real-time Kafka Streaming', 'HDFS Distributed Storage', 'Hive Data Warehousing'],
  },
  {
    icon: Brain,
    title: 'Deep Reinforcement Learning',
    color: 'purple',
    description: 'Training intelligent agents that learn optimal treatment strategies through interaction with simulated clinical environments.',
    features: ['Deep Q-Networks (DQN)', 'Actor-Critic Methods (A3C)', 'Policy Gradient Optimization', 'Experience Replay'],
  },
  {
    icon: Stethoscope,
    title: 'Clinical Decision Support',
    color: 'cyan',
    description: 'Integrating AI predictions with clinical guidelines to provide evidence-based, real-time decision support to healthcare providers.',
    features: ['Differential Diagnosis', 'Treatment Recommendations', 'Risk Stratification', 'Lab Test Prioritization'],
  },
]

const timeline = [
  { year: '2024 Q1', title: 'Data Collection', description: 'Gathered 50,000+ de-identified patient records from partner hospitals.' },
  { year: '2024 Q2', title: 'Pipeline Setup', description: 'Built distributed big data pipeline with Hadoop, Spark, and Kafka.' },
  { year: '2024 Q3', title: 'Model Training', description: 'Trained DRL models achieving 94.23% accuracy on clinical decision tasks.' },
  { year: '2024 Q4', title: 'CDSS Integration', description: 'Integrated DRL engine into clinical decision support system with real-time inference.' },
]

export default function About() {
  return (
    <div className="py-20 px-4">
      <div className="max-w-6xl mx-auto">
        <SectionHeader
          title="About the Project"
          subtitle="Bridging the gap between Big Data Analytics and Clinical Decision Making through Deep Reinforcement Learning"
        />

        {/* Problem Statement */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-16"
        >
          <GlassCard gradient>
            <h3 className="font-space text-xl font-bold text-cyan mb-4">Problem Statement</h3>
            <p className="text-text-secondary leading-relaxed text-lg">
              Healthcare systems generate enormous volumes of data daily, yet clinical decision-making
              often relies on individual physician experience and static guidelines. This project addresses
              the critical need for intelligent systems that can process massive clinical datasets in
              real-time and provide evidence-based decision support using advanced Deep Reinforcement
              Learning techniques.
            </p>
          </GlassCard>
        </motion.div>

        {/* Research Objectives */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-16"
        >
          <GlassCard>
            <h3 className="font-space text-xl font-bold text-purple mb-4">Research Objectives</h3>
            <ul className="space-y-3">
              {[
                'Design a scalable big data pipeline for real-time clinical data processing',
                'Develop DRL models optimized for clinical decision-making tasks',
                'Build an integrated CDSS that provides actionable treatment recommendations',
                'Evaluate system performance against traditional ML approaches',
                'Ensure interpretability and explainability of AI-driven decisions',
              ].map((obj, i) => (
                <li key={i} className="flex items-start gap-3 text-text-secondary">
                  <ArrowRight className="w-5 h-5 text-purple mt-0.5 shrink-0" />
                  <span>{obj}</span>
                </li>
              ))}
            </ul>
          </GlassCard>
        </motion.div>

        {/* Three Pillars */}
        <SectionHeader title="Three Pillars" subtitle="The foundational components powering our clinical decision support system" accent="purple" />
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-16">
          {pillars.map((pillar, i) => {
            const Icon = pillar.icon
            return (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.15 }}
              >
                <GlassCard className="h-full" gradient>
                  <div className={`w-14 h-14 rounded-xl ${colorMap[pillar.color].bg} flex items-center justify-center mb-4`}>
                    <Icon className={`w-7 h-7 ${colorMap[pillar.color].icon}`} />
                  </div>
                  <h3 className="font-space text-xl font-bold mb-3">{pillar.title}</h3>
                  <p className="text-text-secondary text-sm leading-relaxed mb-4">{pillar.description}</p>
                  <ul className="space-y-2">
                    {pillar.features.map((f, j) => (
                      <li key={j} className="flex items-center gap-2 text-sm text-text-secondary">
                        <div className={`w-1.5 h-1.5 rounded-full ${colorMap[pillar.color].dot}`} />
                        {f}
                      </li>
                    ))}
                  </ul>
                </GlassCard>
              </motion.div>
            )
          })}
        </div>

        {/* Data Flow Timeline */}
        <SectionHeader title="Project Timeline" subtitle="Key milestones in our research journey" />
        <div className="relative">
          <div className="absolute left-4 md:left-1/2 top-0 bottom-0 w-0.5 bg-gradient-to-b from-cyan via-purple to-cyan/0" />
          {timeline.map((item, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, x: i % 2 === 0 ? -30 : 30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              className={`relative flex items-center mb-8 ${i % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse'}`}
            >
              <div className="hidden md:block md:w-1/2" />
              <div className="absolute left-4 md:left-1/2 w-3 h-3 rounded-full bg-cyan border-2 border-bg-primary transform -translate-x-1/2 z-10" />
              <div className="ml-12 md:ml-0 md:w-1/2 md:px-8">
                <GlassCard>
                  <div className="text-xs font-bold text-cyan mb-1">{item.year}</div>
                  <h4 className="font-space font-semibold text-lg mb-2">{item.title}</h4>
                  <p className="text-text-secondary text-sm">{item.description}</p>
                </GlassCard>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  )
}
