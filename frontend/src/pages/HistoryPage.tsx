import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../api/client'

interface SessionSummary {
  id: string
  case_id: string
  case_title?: string
  status: string
  started_at: string
  completed_at: string | null
}

interface EvalSummary {
  overall_score: number
  session_id: string
}

const STATUS_CONFIG: Record<string, { label: string; bg: string; color: string; emoji: string }> = {
  in_progress: { label: '进行中', bg: 'bg-amber-100', color: 'text-amber-700', emoji: '💬' },
  completed: { label: '已完成', bg: 'bg-emerald-100', color: 'text-emerald-700', emoji: '✅' },
  abandoned: { label: '已放弃', bg: 'bg-gray-100', color: 'text-gray-500', emoji: '🚫' },
}

export default function HistoryPage() {
  const [sessions, setSessions] = useState<SessionSummary[]>([])
  const [evaluations, setEvaluations] = useState<Record<string, EvalSummary>>({})
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.get<SessionSummary[]>('/sessions').then(async (data) => {
      setSessions(data)
      const evals: Record<string, EvalSummary> = {}
      await Promise.all(
        data
          .filter((s) => s.status === 'completed')
          .map(async (s) => {
            try {
              const e = await api.get<EvalSummary>(`/sessions/${s.id}/evaluation`)
              evals[s.id] = e
            } catch {
              // No evaluation yet
            }
          })
      )
      setEvaluations(evals)
      setLoading(false)
    }).catch(() => setLoading(false))
  }, [])

  const formatDate = (iso: string) => {
    const d = new Date(iso)
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')} ${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')}`
  }

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 animate-fade-in">
      <div className="flex items-baseline gap-4 mb-8">
        <h2 className="serif text-3xl font-bold text-ink">训练记录</h2>
        {!loading && (
          <span className="text-sm text-ink-light/50 bg-gray-100 px-2.5 py-0.5 rounded-full font-medium">
            {sessions.length} 条记录
          </span>
        )}
      </div>

      {loading ? (
        <div className="space-y-3 stagger">
          {[...Array(4)].map((_, i) => (
            <div key={i} className="bg-white rounded-2xl p-5 border border-paper-dark animate-pulse">
              <div className="flex gap-4">
                <div className="w-10 h-10 bg-gray-200 rounded-xl shrink-0" />
                <div className="flex-1">
                  <div className="h-4 bg-gray-200 rounded w-48 mb-2" />
                  <div className="h-3 bg-gray-100 rounded w-32" />
                </div>
              </div>
            </div>
          ))}
        </div>
      ) : sessions.length === 0 ? (
        <div className="text-center py-20">
          <div className="w-20 h-20 bg-gray-100 rounded-3xl flex items-center justify-center text-4xl mx-auto mb-5">
            📋
          </div>
          <p className="text-ink font-semibold text-lg mb-2">还没有训练记录</p>
          <p className="text-ink-light text-sm mb-8">开始第一次模拟问诊，积累你的临床经验</p>
          <Link
            to="/cases"
            className="inline-flex items-center gap-2 px-7 py-3 bg-primary text-white rounded-2xl hover:bg-primary-dark transition-all font-semibold no-underline shadow-sm hover:shadow-md hover:shadow-primary/20"
          >
            浏览病例库
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
              <path d="M5 12h14M12 5l7 7-7 7" />
            </svg>
          </Link>
        </div>
      ) : (
        /* Mobile card list */
        <div className="sm:hidden space-y-3 stagger">
          {sessions.map((s) => {
            const status = STATUS_CONFIG[s.status] || STATUS_CONFIG.abandoned
            const ev = evaluations[s.id]
            return (
              <Link
                key={s.id}
                to={s.status === 'in_progress' ? `/consultation/${s.id}` : s.status === 'completed' ? `/evaluation/${s.id}` : '#'}
                className={`block bg-white rounded-2xl p-4 border border-paper-dark hover:shadow-md transition-all duration-200 no-underline ${s.status === 'abandoned' ? 'pointer-events-none' : ''}`}
              >
                <div className="flex items-center gap-3 mb-3">
                  <span className={`w-8 h-8 ${status.bg} rounded-xl flex items-center justify-center text-sm`}>
                    {status.emoji}
                  </span>
                  <div className="flex-1 min-w-0">
                    <p className="font-bold text-ink text-sm truncate">{s.case_title || '未知病例'}</p>
                    <p className="text-xs text-ink-light/50">{formatDate(s.started_at)}</p>
                  </div>
                  <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${status.bg} ${status.color}`}>
                    {status.label}
                  </span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-sm text-ink-light">
                    {ev ? (
                      <span className={`font-bold ${ev.overall_score >= 80 ? 'text-emerald-600' : ev.overall_score >= 60 ? 'text-amber-600' : 'text-red-500'}`}>
                        {ev.overall_score}分
                      </span>
                    ) : s.status === 'completed' ? (
                      '未评估'
                    ) : (
                      ''
                    )}
                  </span>
                  <span className="text-primary text-sm font-semibold">
                    {s.status === 'in_progress' ? '继续问诊 →' : s.status === 'completed' ? (ev ? '查看报告 →' : '生成报告 →') : ''}
                  </span>
                </div>
              </Link>
            )
          })}
        </div>

        /* Desktop table */
      )}
      {sessions.length > 0 && (
        <div className="hidden sm:block bg-white rounded-2xl border border-paper-dark overflow-hidden shadow-sm">
          <table className="w-full">
            <thead>
              <tr className="border-b border-gray-100 bg-gray-50/50">
                <th className="text-left px-5 py-3.5 text-xs font-semibold text-ink-light/50 uppercase tracking-wider">病例</th>
                <th className="text-left px-5 py-3.5 text-xs font-semibold text-ink-light/50 uppercase tracking-wider">状态</th>
                <th className="text-left px-5 py-3.5 text-xs font-semibold text-ink-light/50 uppercase tracking-wider">开始时间</th>
                <th className="text-left px-5 py-3.5 text-xs font-semibold text-ink-light/50 uppercase tracking-wider">评分</th>
                <th className="text-right px-5 py-3.5 text-xs font-semibold text-ink-light/50 uppercase tracking-wider">操作</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-50">
              {sessions.map((s) => {
                const status = STATUS_CONFIG[s.status] || STATUS_CONFIG.abandoned
                const ev = evaluations[s.id]
                return (
                  <tr key={s.id} className="hover:bg-gray-50/50 transition-colors">
                    <td className="px-5 py-4">
                      <div className="flex items-center gap-2.5">
                        <span className={`w-7 h-7 ${status.bg} rounded-lg flex items-center justify-center text-xs`}>
                          {status.emoji}
                        </span>
                        <p className="serif font-bold text-ink text-sm">{s.case_title || '未知病例'}</p>
                      </div>
                    </td>
                    <td className="px-5 py-4">
                      <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${status.bg} ${status.color}`}>
                        {status.label}
                      </span>
                    </td>
                    <td className="px-5 py-4 text-sm text-ink-light">
                      {formatDate(s.started_at)}
                    </td>
                    <td className="px-5 py-4">
                      {ev ? (
                        <span className={`serif font-bold text-sm ${
                          ev.overall_score >= 80 ? 'text-emerald-600' : ev.overall_score >= 60 ? 'text-amber-600' : 'text-red-500'
                        }`}>
                          {ev.overall_score}分
                        </span>
                      ) : s.status === 'completed' ? (
                        <span className="text-xs text-ink-light/40">待生成</span>
                      ) : (
                        <span className="text-xs text-ink-light/20">--</span>
                      )}
                    </td>
                    <td className="px-5 py-4 text-right">
                      {s.status === 'in_progress' ? (
                        <Link
                          to={`/consultation/${s.id}`}
                          className="text-sm text-primary hover:text-primary-dark font-semibold no-underline"
                        >
                          继续问诊
                        </Link>
                      ) : s.status === 'completed' ? (
                        <Link
                          to={`/evaluation/${s.id}`}
                          className="text-sm text-primary hover:text-primary-dark font-semibold no-underline"
                        >
                          {ev ? '查看报告' : '生成报告'}
                        </Link>
                      ) : (
                        <span className="text-sm text-ink-light/20">--</span>
                      )}
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}
