import { Link, useLocation } from 'react-router-dom'

const NAV = [
  { to: '/', label: '首页', icon: '🏠' },
  { to: '/cases', label: '病例库', icon: '📋' },
  { to: '/history', label: '训练记录', icon: '📊' },
]

export default function Header() {
  const loc = useLocation()

  return (
    <header className="bg-white/80 backdrop-blur-md border-b border-paper-dark sticky top-0 z-20 shadow-sm">
      <div className="max-w-6xl mx-auto px-5 h-15 flex items-center gap-8">
        <Link
          to="/"
          className="flex items-center gap-2.5 no-underline group"
        >
          <img src="/logo.png" alt="MedRole" className="w-8 h-8 rounded-lg shadow-sm shadow-primary/20 group-hover:shadow-md group-hover:shadow-primary/30 transition-shadow" />
          <span className="serif font-black text-xl text-ink tracking-tight">
            Med<span className="text-primary">Role</span>
          </span>
        </Link>

        <nav className="flex gap-1.5">
          {NAV.map((n) => {
            const active = loc.pathname === n.to
            return (
              <Link
                key={n.to}
                to={n.to}
                className={`relative px-3.5 py-1.5 rounded-lg text-sm font-medium transition-all duration-200 no-underline ${
                  active
                    ? 'text-primary bg-primary/8'
                    : 'text-ink-light hover:text-ink hover:bg-gray-100'
                }`}
              >
                <span className="hidden sm:inline mr-1.5">{n.icon}</span>
                {n.label}
                {active && (
                  <span className="absolute bottom-0 left-1/2 -translate-x-1/2 w-5 h-0.5 bg-primary rounded-full" />
                )}
              </Link>
            )
          })}
        </nav>
      </div>
    </header>
  )
}
