import { Link } from 'react-router-dom'
import type { CaseItem } from '../../types'

const DIFF_MAP: Record<string, { label: string; color: string; bg: string }> = {
  beginner: { label: '初级', color: 'text-emerald-700', bg: 'bg-emerald-100' },
  intermediate: { label: '中级', color: 'text-amber-700', bg: 'bg-amber-100' },
  advanced: { label: '高级', color: 'text-red-700', bg: 'bg-red-100' },
}

interface Props {
  item: CaseItem
}

export default function CaseCard({ item }: Props) {
  const diff = DIFF_MAP[item.difficulty] || DIFF_MAP.beginner
  const p = item.patient_profile

  return (
    <Link
      to={`/consultation/new?caseId=${item.id}`}
      className="group block bg-white rounded-2xl p-5 border border-paper-dark hover:shadow-lg hover:border-primary/30 transition-all duration-300 no-underline hover:-translate-y-0.5"
    >
      <div className="flex items-center gap-2 mb-3">
        <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${diff.bg} ${diff.color}`}>
          {diff.label}
        </span>
        <span className="text-xs text-ink-light/60 bg-gray-100 px-2 py-0.5 rounded-full">
          {item.department}
        </span>
      </div>
      <h3 className="serif text-lg font-bold text-ink mb-2 leading-tight group-hover:text-primary transition-colors">
        {item.title}
      </h3>
      <p className="text-sm text-ink-light mb-4 line-clamp-2 leading-relaxed">{item.chief_complaint}</p>
      <div className="flex items-center gap-3 text-xs text-ink-light/60 pt-3 border-t border-gray-100">
        <span className="flex items-center gap-1">
          <span className="text-sm">👤</span> {p.name}
        </span>
        <span>{p.age}岁</span>
        <span>{p.gender}</span>
        <span className="ml-auto text-primary font-semibold opacity-0 group-hover:opacity-100 transition-all duration-300 group-hover:translate-x-0.5">
          开始接诊 →
        </span>
      </div>
    </Link>
  )
}
