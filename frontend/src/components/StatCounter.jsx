import { motion } from 'framer-motion'
import { useCountUp } from '../hooks/useCountUp'

export default function StatCounter({ label, value, suffix = '' }) {
  const count = useCountUp(value, 2000)

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      className="text-center"
    >
      <div className="font-space text-4xl sm:text-5xl font-bold text-cyan text-glow-cyan">
        {count}{suffix}
      </div>
      <div className="text-text-secondary mt-2 text-sm">{label}</div>
    </motion.div>
  )
}
