import { useState, useEffect, useRef } from 'react'

export function useCountUp(end, duration = 2000, startOnMount = true) {
  const [count, setCount] = useState(0)
  const startedRef = useRef(false)

  useEffect(() => {
    if (!startOnMount || startedRef.current) return
    startedRef.current = true

    let startTime = null
    const step = (timestamp) => {
      if (!startTime) startTime = timestamp
      const progress = Math.min((timestamp - startTime) / duration, 1)
      setCount(Math.floor(progress * end))
      if (progress < 1) requestAnimationFrame(step)
    }
    requestAnimationFrame(step)
  }, [end, duration, startOnMount])

  return count
}
