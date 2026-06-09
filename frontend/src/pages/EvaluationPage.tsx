import { useEffect, useState } from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'
import { api } from '../api/client'
import RadarChartView from '../components/evaluation/RadarChartView'
import DimensionDetail from '../components/evaluation/DimensionDetail'
import type { Evaluation } from '../types'

export default function EvaluationPage() {
  const { sessionId } = useParams<{ sessionId: string }>()
  const navigate = useNavigate()
  const [evaluation, setEvaluation] = useState<Evaluation | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [generating, setGenerating] = useState(false)
  const [retrying, setRetrying] = useState(false)

  const loadEvaluation = () => {
    if (!sessionId) return
    setLoading(true)
    setError('')

    api.get<Evaluation>(`/sessions/${sessionId}/evaluation`)
      .then((data) => {
        setEvaluation(data)
        setLoading(false)
      })
      .catch(async () => {
        setGenerating(true)
        try {
          const data = await api.post<Evaluation>(`/sessions/${sessionId}/evaluate`)
          setEvaluation(data)
        } catch (e: any) {
          setError(e.message || '评估失败')
        } finally {
          setLoading(false)
          setGenerating(false)
        }
      })
  }

  useEffect(() => {
    loadEvaluation()
  }, [sessionId])

  const handleRetry = () => {
    setRetrying(true)
    api.post<Evaluation>(`/sessions/${sessionId}/evaluate`)
      .then((data) => {
        setEvaluation(data)
        setError('')
      })
      .catch((e: any) => {
        setError(e.message || '评估失败')
      })
      .finally(() => setRetrying(false))
  }

  if (loading || generating) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center animate-fade-in">
        <div className="relative w-16 h-16 mx-auto mb-6">
          <div className="absolute inset-0 border-4 border-primary/15 rounded-full" />
          <div className="absolute inset-0 border-4 border-primary border-t-transparent rounded-full animate-spin" />
        </div>
        <p className="text-ink font-semibold text-lg mb-2">
          {generating ? 'AI 考官正在分析您的问诊表现' : '加载评估报告'}
        </p>
        <p className="text-ink-light text-sm">
          {generating ? 'DeepSeek 正在对问诊对话进行四维 OSCE 评估，约需 15-30 秒…' : '请稍候…'}
        </p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center animate-fade-in">
        <div className="text-5xl mb-4">⚠️</div>
        <p className="text-ink font-semibold text-lg mb-2">评估生成失败</p>
        <p className="text-ink-light text-sm mb-6">{error}</p>
        <button
          onClick={handleRetry}
          disabled={retrying}
          className="px-6 py-2.5 bg-primary text-white rounded-xl hover:bg-primary-dark transition-all cursor-pointer font-medium disabled:opacity-50"
        >
          {retrying ? '重试中…' : '重新生成评估'}
        </button>
      </div>
    )
  }

  if (!evaluation) return null

  const { dimensions } = evaluation
  const scoreColor = evaluation.overall_score >= 80 ? 'text-emerald-600' : evaluation.overall_score >= 60 ? 'text-amber-600' : 'text-red-500'
  const scoreBg = evaluation.overall_score >= 80 ? 'bg-emerald-50' : evaluation.overall_score >= 60 ? 'bg-amber-50' : 'bg-red-50'
  const gradeLabel = evaluation.overall_score >= 85 ? '优秀' : evaluation.overall_score >= 70 ? '良好' : evaluation.overall_score >= 60 ? '及格' : '需要加强'
  const gradeEmoji = evaluation.overall_score >= 85 ? '🏆' : evaluation.overall_score >= 70 ? '👍' : evaluation.overall_score >= 60 ? '📚' : '💪'

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 animate-fade-in">
      {/* Breadcrumb */}
      <div className="flex items-center gap-4 mb-8">
        <button
          onClick={() => navigate('/history')}
          className="text-ink-light/60 hover:text-ink transition-colors text-sm cursor-pointer flex items-center gap-1"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M19 12H5M12 19l-7-7 7-7" />
          </svg>
          返回记录
        </button>
        <span className="text-ink-light/20">|</span>
        <h2 className="serif text-xl font-bold text-ink">OSCE 评估报告</h2>
      </div>

      {/* Overall Score Card */}
      <div className={`${scoreBg} rounded-3xl p-10 text-center mb-8 border border-paper-dark animate-scale-in`}>
        <p className="text-xs font-medium uppercase tracking-widest text-ink-light/50 mb-4">综合评分</p>
        <div className="inline-flex items-center gap-3 mb-2">
          <span className="text-4xl">{gradeEmoji}</span>
          <span className={`serif text-8xl font-black ${scoreColor}`}>
            {evaluation.overall_score}
          </span>
        </div>
        <p className={`text-xl font-bold ${scoreColor} mb-5`}>{gradeLabel}</p>
        <p className="text-ink-light max-w-lg mx-auto leading-relaxed text-sm">
          {evaluation.summary}
        </p>
      </div>

      {/* Radar Chart */}
      <div className="mb-8 animate-fade-in-up">
        <RadarChartView
          completeness={dimensions.completeness.score}
          communication={dimensions.communication.score}
          clinicalThinking={dimensions.clinical_thinking.score}
          objective={dimensions.objective.score}
        />
      </div>

      {/* Dimension Details */}
      <div className="space-y-3 mb-8 stagger">
        <DimensionDetail title="问诊完整性" dimension={dimensions.completeness} defaultOpen />
        <DimensionDetail title="医患沟通" dimension={dimensions.communication} />
        <DimensionDetail title="临床思维" dimension={dimensions.clinical_thinking} />
        <DimensionDetail title="客观评分" dimension={dimensions.objective} />
      </div>

      {/* Diagnosis guess */}
      <div className="bg-white rounded-2xl p-5 border border-paper-dark mb-8 shadow-sm">
        <div className="flex items-center gap-2 mb-2">
          <span className="text-lg">🔍</span>
          <h4 className="text-xs font-semibold uppercase tracking-wider text-ink-light/50">AI 推测你的诊断方向</h4>
        </div>
        <p className="text-sm text-ink-light leading-relaxed">{evaluation.diagnosis_guess}</p>
      </div>

      {/* Actions */}
      <div className="flex gap-3 justify-center">
        <Link
          to="/cases"
          className="px-7 py-3 bg-primary text-white rounded-2xl hover:bg-primary-dark transition-all font-semibold no-underline shadow-sm hover:shadow-md hover:shadow-primary/20"
        >
          练习下一个病例
        </Link>
        <Link
          to="/history"
          className="px-7 py-3 bg-white text-ink-light rounded-2xl border border-gray-200 hover:bg-gray-50 transition-all font-medium no-underline"
        >
          查看训练记录
        </Link>
      </div>
    </div>
  )
}
