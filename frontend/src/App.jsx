import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom'
import { AnimatePresence, motion } from 'framer-motion'
import { ThemeProvider } from './context/ThemeContext'
import MainLayout from './layouts/MainLayout'
import Home from './pages/Home'
import About from './pages/About'
import Architecture from './pages/Architecture'
import BigData from './pages/BigData'
import DRL from './pages/DRL'
import Demo from './pages/Demo'
import Results from './pages/Results'
import Team from './pages/Team'

function AnimatedRoutes() {
  const location = useLocation()
  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={location.pathname}
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -10 }}
        transition={{ duration: 0.3 }}
      >
        <Routes location={location}>
          <Route element={<MainLayout />}>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/architecture" element={<Architecture />} />
            <Route path="/big-data" element={<BigData />} />
            <Route path="/drl" element={<DRL />} />
            <Route path="/demo" element={<Demo />} />
            <Route path="/results" element={<Results />} />
            <Route path="/team" element={<Team />} />
          </Route>
        </Routes>
      </motion.div>
    </AnimatePresence>
  )
}

export default function App() {
  return (
    <ThemeProvider>
      <Router>
        <AnimatedRoutes />
      </Router>
    </ThemeProvider>
  )
}
