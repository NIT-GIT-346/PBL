import { motion } from 'framer-motion'
import { BookOpen, Calendar, Award } from 'lucide-react'
import GlassCard from '../components/GlassCard'
import SectionHeader from '../components/SectionHeader'
import { TEAM_MEMBERS, PROJECT_TIMELINE, REFERENCES } from '../data/mockData'

export default function Team() {
  return (
    <div className="py-20 px-4">
      <div className="max-w-6xl mx-auto">
        <SectionHeader
          title="Research Team"
          subtitle="Meet the researchers and engineers behind the Clinical DSS project"
        />

        {/* Supervisor */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mb-12"
        >
          <GlassCard gradient className="text-center max-w-lg mx-auto">
            <div className="w-20 h-20 rounded-full bg-gradient-to-br from-cyan to-purple flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl font-bold font-space text-white">RK</span>
            </div>
            <h3 className="font-space text-xl font-bold">Dr. Rajesh Kumar</h3>
            <p className="text-cyan text-sm font-medium mb-2">Project Supervisor</p>
            <p className="text-text-secondary text-sm">
              Professor of Computer Science & AI • 15+ years in Healthcare AI Research
            </p>
            <div className="flex items-center justify-center gap-2 mt-3">
              <Award className="w-4 h-4 text-purple" />
              <span className="text-xs text-text-secondary">Department of Computer Science & Engineering</span>
            </div>
          </GlassCard>
        </motion.div>

        {/* Team Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
          {TEAM_MEMBERS.map((member, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
            >
              <GlassCard className="text-center h-full">
                <div className="w-16 h-16 rounded-full bg-gradient-to-br from-cyan/20 to-purple/20 border border-cyan/20 flex items-center justify-center mx-auto mb-4">
                  <span className="font-space font-bold text-lg text-cyan">{member.avatar}</span>
                </div>
                <h4 className="font-space font-bold text-lg">{member.name}</h4>
                <p className="text-purple text-sm font-medium mb-1">{member.role}</p>
                <p className="text-text-secondary text-xs">{member.expertise}</p>
              </GlassCard>
            </motion.div>
          ))}
        </div>

        {/* Project Timeline */}
        <SectionHeader title="Project Timeline" subtitle="Milestones and deliverables throughout the research period" accent="purple" />
        <div className="mb-16">
          <div className="relative">
            <div className="absolute left-4 md:left-1/2 top-0 bottom-0 w-0.5 bg-gradient-to-b from-cyan via-purple to-cyan/30 transform md:-translate-x-1/2" />
            {PROJECT_TIMELINE.map((item, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
                className={`relative flex mb-6 ${i % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse'}`}
              >
                <div className="hidden md:block md:w-1/2" />
                <div className="absolute left-4 md:left-1/2 w-4 h-4 rounded-full border-2 border-bg-primary transform -translate-x-1/2 z-10" style={{
                  backgroundColor: item.status === 'completed' ? '#00D4FF' : item.status === 'active' ? '#7C3AED' : '#374151',
                }} />
                <div className="ml-12 md:ml-0 md:w-1/2 md:px-8">
                  <GlassCard>
                    <div className="flex items-center gap-2 mb-2">
                      <Calendar className="w-4 h-4 text-purple" />
                      <span className="text-xs text-purple font-bold">{item.period}</span>
                      {item.status === 'active' && (
                        <span className="px-2 py-0.5 rounded-full bg-purple/20 text-purple text-xs font-bold animate-pulse">Active</span>
                      )}
                    </div>
                    <h4 className="font-space font-semibold">{item.phase}: {item.title}</h4>
                  </GlassCard>
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        {/* References */}
        <SectionHeader title="References" subtitle="Key publications and resources that informed this research" />
        <GlassCard>
          <div className="space-y-4">
            {REFERENCES.map((ref, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, x: -10 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.08 }}
                className="flex items-start gap-3 text-sm text-text-secondary"
              >
                <BookOpen className="w-4 h-4 text-cyan shrink-0 mt-0.5" />
                <span className="leading-relaxed">[{i + 1}] {ref}</span>
              </motion.div>
            ))}
          </div>
        </GlassCard>
      </div>
    </div>
  )
}
