export default function SkeletonLoader({ lines = 3, className = '' }) {
  return (
    <div className={`space-y-3 ${className}`}>
      {Array.from({ length: lines }).map((_, i) => (
        <div
          key={i}
          className="skeleton rounded-lg h-4"
          style={{ width: `${100 - i * 15}%` }}
        />
      ))}
    </div>
  )
}

export function SkeletonCard() {
  return (
    <div className="glass-card p-6 space-y-4">
      <div className="skeleton rounded-lg h-6 w-1/3" />
      <div className="skeleton rounded-lg h-4 w-full" />
      <div className="skeleton rounded-lg h-4 w-4/5" />
      <div className="skeleton rounded-lg h-4 w-2/3" />
    </div>
  )
}
