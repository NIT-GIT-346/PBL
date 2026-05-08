import { motion } from 'framer-motion'

export default function SectionHeader({ title, subtitle, accent = 'cyan' }) {
  const accentClass = accent === 'cyan' ? 'text-cyan' : 'text-purple'
  const lineClass = accent === 'cyan' ? 'from-cyan/50' : 'from-purple/50'

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: 0.6 }}
      className="text-center mb-12"
    >
      <h2 className={`font-space text-3xl sm:text-4xl font-bold mb-4 ${accentClass}`}>
        {title}
      </h2>
      {subtitle && (
        <p className="text-text-secondary max-w-2xl mx-auto text-lg">{subtitle}</p>
      )}
      <div className={`w-24 h-1 mx-auto mt-6 rounded-full bg-gradient-to-r ${lineClass} to-transparent`} />
    </motion.div>
  )
}
