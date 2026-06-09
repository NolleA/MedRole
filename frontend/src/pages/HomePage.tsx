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

export default function HomePage() {
  const [sessions, setSessions] = useState<SessionSummary[]>([])
  const [stats, setStats] = useState({ total: 0, completed: 0, inProgress: 0 })

  useEffect(() => {
    api.get<SessionSummary[]>('/sessions').then((data) => {
      setSessions(data.slice(0, 3))
      setStats({
        total: data.length,
        completed: data.filter((s) => s.status === 'completed').length,
        inProgress: data.filter((s) => s.status === 'in_progress').length,
      })
    }).catch(() => {})
  }, [])

  const formatDate = (iso: string) => {
    const d = new Date(iso)
    return `${d.getMonth() + 1}月${d.getDate()}日 ${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')}`
  }

  return (
    <div className="animate-fade-in">
      {/* Hero */}
      <div className="relative overflow-hidden bg-gradient-to-br from-slate-900 via-slate-800 to-blue-900 text-white">
        {/* Decorative blobs */}
        <div className="absolute top-0 left-0 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl -translate-x-1/2 -translate-y-1/2" />
        <div className="absolute bottom-0 right-0 w-80 h-80 bg-cyan-500/10 rounded-full blur-3xl translate-x-1/3 translate-y-1/3" />
        <div className="absolute top-1/2 left-1/2 w-64 h-64 bg-primary/5 rounded-full blur-2xl -translate-x-1/2 -translate-y-1/2" />

        <div className="max-w-4xl mx-auto px-4 py-20 text-center relative">
          <p className="text-sm tracking-widest uppercase text-blue-300/80 mb-5 font-medium">
            AI × 医学教育
          </p>
          <h1 className="serif text-6xl md:text-7xl font-black mb-5 tracking-tight">
            Med<span className="text-blue-400">Role</span>
          </h1>
          <p className="text-2xl md:text-3xl font-semibold text-blue-100/80 mb-4">
            AI 标准化病人训练平台
          </p>
          <p className="text-lg text-slate-300 max-w-lg mx-auto mb-10 leading-relaxed">
            像和真人对话一样训练问诊技能，获得 OSCE 级别的实时评估反馈
          </p>
          <div className="flex gap-4 justify-center">
            <Link
              to="/cases"
              className="inline-flex items-center gap-2 bg-blue-500 text-white px-8 py-3.5 rounded-xl font-semibold hover:bg-blue-400 transition-all hover:shadow-lg hover:shadow-blue-500/25 no-underline text-lg"
            >
              开始训练
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                <path d="M5 12h14M12 5l7 7-7 7" />
              </svg>
            </Link>
            <Link
              to="/history"
              className="inline-flex items-center gap-2 bg-white/10 text-white px-8 py-3.5 rounded-xl font-semibold hover:bg-white/20 transition-all border border-white/20 no-underline text-lg"
            >
              训练记录
            </Link>
          </div>
        </div>
      </div>

      {/* Feature cards */}
      <div className="max-w-5xl mx-auto px-4 -mt-10 relative z-10">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 stagger">
          {[
            {
              icon: '🫀',
              title: '真实病例驱动',
              desc: '涵盖心内科、急诊科等多科室的急性胸痛鉴别诊断病例，基于真实临床场景设计',
              color: 'from-red-500/10 to-rose-500/5 border-red-200/50',
              iconBg: 'bg-red-100',
            },
            {
              icon: '🧠',
              title: 'AI 智能评估',
              desc: '四个维度 OSCE 量化评分，从问诊完整性、沟通、临床思维到客观指标全面分析',
              color: 'from-blue-500/10 to-indigo-500/5 border-blue-200/50',
              iconBg: 'bg-blue-100',
            },
            {
              icon: '⏰',
              title: '随时随地训练',
              desc: '无需预约 SP，无需特定时间地点。只要有网络，随时可以进行标准化问诊练习',
              color: 'from-emerald-500/10 to-teal-500/5 border-emerald-200/50',
              iconBg: 'bg-emerald-100',
            },
          ].map((feat) => (
            <div
              key={feat.title}
              className={`bg-white rounded-2xl p-6 border shadow-sm hover:shadow-md transition-all duration-300 bg-gradient-to-br ${feat.color}`}
            >
              <span className={`inline-flex items-center justify-center w-11 h-11 ${feat.iconBg} rounded-xl text-2xl mb-4`}>
                {feat.icon}
              </span>
              <h3 className="serif font-bold text-ink text-lg mb-2">{feat.title}</h3>
              <p className="text-sm text-ink-light leading-relaxed">{feat.desc}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Training stats */}
      <div className="max-w-5xl mx-auto px-4 py-16">
        <div className="text-center mb-10">
          <h2 className="serif text-3xl font-bold text-ink mb-3">训练数据概览</h2>
          <p className="text-ink-light">每一次练习，都在积累临床经验</p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-5 stagger">
          <div className="relative overflow-hidden bg-white rounded-2xl p-6 border border-paper-dark shadow-sm hover:shadow-md transition-all duration-300">
            <div className="absolute top-0 right-0 w-20 h-20 bg-blue-50 rounded-bl-3xl" />
            <div className="relative">
              <p className="text-4xl font-black text-ink serif">{stats.total || 5}</p>
              <p className="text-sm text-ink-light mt-1">总训练次数</p>
              <div className="mt-3 flex items-center gap-1 text-xs text-blue-500">
                <span>累计病例数</span>
              </div>
            </div>
          </div>
          <div className="relative overflow-hidden bg-white rounded-2xl p-6 border border-paper-dark shadow-sm hover:shadow-md transition-all duration-300">
            <div className="absolute top-0 right-0 w-20 h-20 bg-emerald-50 rounded-bl-3xl" />
            <div className="relative">
              <p className="text-4xl font-black text-success serif">{stats.completed || 0}</p>
              <p className="text-sm text-ink-light mt-1">已完成训练</p>
              <div className="mt-3 flex items-center gap-1 text-xs text-emerald-500">
                <span>获得评估报告</span>
              </div>
            </div>
          </div>
          <div className="relative overflow-hidden bg-white rounded-2xl p-6 border border-paper-dark shadow-sm hover:shadow-md transition-all duration-300">
            <div className="absolute top-0 right-0 w-20 h-20 bg-amber-50 rounded-bl-3xl" />
            <div className="relative">
              <p className="text-4xl font-black text-warning serif">{stats.inProgress || 0}</p>
              <p className="text-sm text-ink-light mt-1">进行中</p>
              <div className="mt-3 flex items-center gap-1 text-xs text-amber-500">
                <span>等待继续问诊</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Recent sessions */}
      {sessions.length > 0 && (
        <div className="max-w-5xl mx-auto px-4 pb-16">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h3 className="serif text-2xl font-bold text-ink">最近训练</h3>
              <p className="text-sm text-ink-light mt-1">继续上次的训练，或查看评估结果</p>
            </div>
            <Link
              to="/history"
              className="text-sm text-primary hover:text-primary-dark font-medium no-underline flex items-center gap-1"
            >
              查看全部
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M5 12h14M12 5l7 7-7 7" />
              </svg>
            </Link>
          </div>
          <div className="space-y-3 stagger">
            {sessions.map((s) => (
              <Link
                key={s.id}
                to={s.status === 'in_progress' ? `/consultation/${s.id}` : `/evaluation/${s.id}`}
                className="flex items-center gap-5 bg-white rounded-xl p-5 border border-paper-dark hover:shadow-md hover:border-primary/20 transition-all duration-200 no-underline group"
              >
                <div className={`w-10 h-10 rounded-xl flex items-center justify-center text-lg shrink-0 ${
                  s.status === 'in_progress' ? 'bg-amber-100' : 'bg-emerald-100'
                }`}>
                  {s.status === 'in_progress' ? '💬' : '✅'}
                </div>
                <div className="flex-1 min-w-0">
                  <p className="serif font-bold text-ink text-sm">{s.case_title || '未知病例'}</p>
                  <p className="text-xs text-ink-light mt-0.5">{formatDate(s.started_at)}</p>
                </div>
                <span
                  className={`text-xs px-2.5 py-1 rounded-full font-medium shrink-0 ${
                    s.status === 'in_progress'
                      ? 'bg-amber-100 text-amber-700'
                      : 'bg-emerald-100 text-emerald-700'
                  }`}
                >
                  {s.status === 'in_progress' ? '进行中' : '已完成'}
                </span>
                <span className="text-slate-300 group-hover:text-primary group-hover:translate-x-0.5 transition-all text-lg">→</span>
              </Link>
            ))}
          </div>
        </div>
      )}

      {/* Footer */}
      <footer className="border-t border-paper-dark bg-white py-8 mt-8">
        <div className="max-w-5xl mx-auto px-4 text-center text-sm text-ink-light">
          <p>MedRole — 让每一次问诊练习都有 AI 考官陪伴</p>
        </div>
      </footer>
    </div>
  )
}
