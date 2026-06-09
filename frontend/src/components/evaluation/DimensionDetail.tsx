import { useState } from 'react'
import type { DimensionScore, ObjectiveScore } from '../../types'

interface Props {
  title: string
  dimension: DimensionScore | ObjectiveScore
  defaultOpen?: boolean
}

function isObjective(d: DimensionScore | ObjectiveScore): d is ObjectiveScore {
  return 'items_covered' in d && 'missed_list' in d
}

const scoreConfig = (score: number) => {
  if (score >= 80) return { text: 'text-emerald-600', bg: 'bg-emerald-50', bar: 'bg-emerald-500', ring: 'ring-emerald-200' }
  if (score >= 60) return { text: 'text-amber-600', bg: 'bg-amber-50', bar: 'bg-amber-500', ring: 'ring-amber-200' }
  return { text: 'text-red-500', bg: 'bg-red-50', bar: 'bg-red-500', ring: 'ring-red-200' }
}

export default function DimensionDetail({ title, dimension, defaultOpen = false }: Props) {
  const [open, setOpen] = useState(defaultOpen)
  const c = scoreConfig(dimension.score)

  return (
    <div className="bg-white rounded-2xl border border-paper-dark overflow-hidden shadow-sm hover:shadow-md transition-all duration-200">
      <button
        onClick={() => setOpen(!open)}
        className="w-full px-5 py-4 flex items-center gap-4 text-left hover:bg-gray-50/80 transition-colors cursor-pointer"
      >
        <div className={`w-12 h-12 rounded-2xl ${c.bg} ring-1 ${c.ring} flex items-center justify-center shrink-0`}>
          <span className={`serif text-xl font-black ${c.text}`}>{dimension.score}</span>
        </div>
        <div className="flex-1 min-w-0">
          <h4 className="serif font-bold text-ink text-sm">{title}</h4>
          <div className="w-full h-1.5 bg-gray-100 rounded-full mt-2 overflow-hidden">
            <div
              className={`h-full rounded-full transition-all duration-700 ease-out ${c.bar}`}
              style={{ width: `${dimension.score}%` }}
            />
          </div>
        </div>
        <svg
          className={`w-5 h-5 text-ink-light/30 transition-transform duration-300 ${open ? 'rotate-180' : ''}`}
          fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24"
        >
          <path d="M6 9l6 6 6-6" />
        </svg>
      </button>

      {open && (
        <div className="px-5 pb-5 border-t border-gray-100 pt-4 space-y-4 animate-fade-in">
          {dimension.strengths.length > 0 && (
            <div>
              <p className="text-xs font-semibold text-emerald-600 mb-2 uppercase tracking-wider">做得好的地方</p>
              <ul className="space-y-1.5">
                {dimension.strengths.map((s: string, i: number) => (
                  <li key={i} className="text-sm text-ink-light flex gap-2.5">
                    <span className="text-emerald-500 shrink-0 mt-0.5">✓</span>
                    {s}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {dimension.improvements.length > 0 && (
            <div>
              <p className="text-xs font-semibold text-amber-600 mb-2 uppercase tracking-wider">需要改进</p>
              <ul className="space-y-1.5">
                {dimension.improvements.map((s: string, i: number) => (
                  <li key={i} className="text-sm text-ink-light flex gap-2.5">
                    <span className="text-amber-500 shrink-0 mt-0.5">→</span>
                    {s}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {isObjective(dimension) && (
            <div className="space-y-3">
              {dimension.covered_list && dimension.covered_list.length > 0 && (
                <div>
                  <p className="text-xs font-semibold text-emerald-600 mb-1.5">
                    已覆盖 ({dimension.items_covered}/{dimension.items_total})
                  </p>
                  <div className="flex flex-wrap gap-1.5">
                    {dimension.covered_list.map((s, i) => (
                      <span key={i} className="text-xs bg-emerald-50 text-emerald-700 px-2 py-1 rounded-lg">{s}</span>
                    ))}
                  </div>
                </div>
              )}
              {dimension.missed_list && dimension.missed_list.length > 0 && (
                <div>
                  <p className="text-xs font-semibold text-red-500 mb-1.5">遗漏 ({dimension.missed_list.length}项)</p>
                  <div className="flex flex-wrap gap-1.5">
                    {dimension.missed_list.map((s, i) => (
                      <span key={i} className="text-xs bg-red-50 text-red-600 px-2 py-1 rounded-lg">{s}</span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          {dimension.feedback && (
            <div className="pt-3 border-t border-gray-50">
              <p className="text-xs font-semibold text-ink-light/40 mb-1.5 uppercase tracking-wider">详细反馈</p>
              <p className="text-sm text-ink-light leading-relaxed">{dimension.feedback}</p>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
