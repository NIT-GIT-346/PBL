import { motion } from 'framer-motion'

export default function LoadingBar({ isLoading }) {
  if (!isLoading) return null
  return (
    <div className="fixed top-0 left-0 right-0 z-[60] h-1 bg-transparent">
      <motion.div
        className="h-full bg-gradient-to-r from-cyan via-purple to-cyan"
        initial={{ x: '-100%' }}
        animate={{ x: '100%' }}
        transition={{ repeat: Infinity, duration: 1.5, ease: 'linear' }}
      />
    </div>
  )
}
