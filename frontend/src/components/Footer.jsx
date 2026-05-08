import { Brain, GitBranch, Mail } from 'lucide-react'
import { Link } from 'react-router-dom'

export default function Footer() {
  return (
    <footer className="border-t border-border/50 bg-bg-card/50 mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <div className="flex items-center gap-2 mb-4">
              <Brain className="w-6 h-6 text-cyan" />
              <span className="font-space font-bold text-lg">Clinical DSS</span>
            </div>
            <p className="text-text-secondary text-sm leading-relaxed">
              Deep Reinforcement Learning-based Clinical Decision Support System using Big Data Analytics.
            </p>
          </div>
          <div>
            <h4 className="font-space font-semibold mb-4">Quick Links</h4>
            <div className="space-y-2">
              <Link to="/about" className="block text-sm text-text-secondary hover:text-cyan transition-colors">About Project</Link>
              <Link to="/demo" className="block text-sm text-text-secondary hover:text-cyan transition-colors">Live Demo</Link>
              <Link to="/results" className="block text-sm text-text-secondary hover:text-cyan transition-colors">Results</Link>
              <Link to="/team" className="block text-sm text-text-secondary hover:text-cyan transition-colors">Team</Link>
            </div>
          </div>
          <div>
            <h4 className="font-space font-semibold mb-4">Contact</h4>
            <div className="space-y-2">
              <a href="#" className="flex items-center gap-2 text-sm text-text-secondary hover:text-cyan transition-colors">
                <Mail className="w-4 h-4" /> research@clinical-dss.ai
              </a>
              <a href="#" className="flex items-center gap-2 text-sm text-text-secondary hover:text-cyan transition-colors">
                <GitBranch className="w-4 h-4" /> GitHub Repository
              </a>
            </div>
          </div>
        </div>
        <div className="border-t border-border/50 mt-8 pt-8 text-center text-sm text-text-secondary">
          © 2024 Clinical DSS Research Project. All rights reserved.
        </div>
      </div>
    </footer>
  )
}
