import { motion } from 'framer-motion'

export default function GlassCard({ children, className = '', hover = true, gradient = false, ...props }) {
  return (
    <motion.div
      className={`glass-card ${hover ? 'glass-card-hover' : ''} ${gradient ? 'gradient-border' : ''} p-6 ${className}`}
      whileHover={hover ? { y: -2 } : {}}
      transition={{ duration: 0.2 }}
      {...props}
    >
      {children}
    </motion.div>
  )
}
