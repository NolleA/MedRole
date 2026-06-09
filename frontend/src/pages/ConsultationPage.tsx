import { useEffect, useRef, useState } from 'react'
import { useParams, useSearchParams, useNavigate } from 'react-router-dom'
import { useSessionStore } from '../store/sessionStore'
import ChatContainer from '../components/chat/ChatContainer'
import ChatInput from '../components/chat/ChatInput'
import { api } from '../api/client'
import type { CaseDetail } from '../types'

export default function ConsultationPage() {
  const { sessionId } = useParams<{ sessionId: string }>()
  const [searchParams] = useSearchParams()
  const navigate = useNavigate()
  const {
    messages, isLoading, currentSessionId, sessionStatus,
    startSession, sendMessage, endSession, loadSession, resetSession,
  } = useSessionStore()

  const [caseInfo, setCaseInfo] = useState<CaseDetail | null>(null)
  const [showEndConfirm, setShowEndConfirm] = useState(false)
  const containerRef = useRef<HTMLDivElement>(null)

  // Start new session or load existing
  useEffect(() => {
    const caseId = searchParams.get('caseId')
    if (sessionId === 'new' && caseId) {
      api.get<CaseDetail>(`/cases/${caseId}`).then(setCaseInfo)
      startSession(caseId).then((sid) => {
        navigate(`/consultation/${sid}`, { replace: true })
      })
    } else if (sessionId && sessionId !== 'new') {
      loadSession(sessionId)
      api.get(`/sessions/${sessionId}`).then((s: any) => {
        if (s.case_id) {
          api.get<CaseDetail>(`/cases/${s.case_id}`).then(setCaseInfo)
        }
      })
    }

    return () => {
      // Don't reset on navigation to evaluation
    }
  }, [sessionId])

  // Scroll to bottom on new messages
  useEffect(() => {
    if (containerRef.current) {
      containerRef.current.scrollTop = containerRef.current.scrollHeight
    }
  }, [messages])

  const handleSend = (content: string) => {
    sendMessage(content)
  }

  const handleEndSession = async () => {
    await endSession()
    if (currentSessionId) {
      navigate(`/evaluation/${currentSessionId}`)
    }
  }

  if (!caseInfo && sessionId !== 'new') {
    return (
      <div className="max-w-4xl mx-auto px-4 py-16 text-center animate-fade-in">
        <div className="w-12 h-12 border-4 border-primary/15 border-t-primary rounded-full animate-spin mx-auto mb-4" />
        <p className="text-ink-light">加载问诊会话…</p>
      </div>
    )
  }

  return (
    <div className="h-[calc(100vh-60px)] flex flex-col">
      {/* Top bar */}
      <div className="bg-white/80 backdrop-blur-md border-b border-gray-100 px-4 py-3 flex items-center gap-4 shrink-0 shadow-sm">
        <button
          onClick={() => navigate('/cases')}
          className="text-ink-light/60 hover:text-ink transition-colors cursor-pointer text-sm flex items-center gap-1"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M19 12H5M12 19l-7-7 7-7" />
          </svg>
          返回
        </button>
        {caseInfo && (
          <>
            <span className="text-gray-200">|</span>
            <div className="flex items-center gap-3">
              <span className="w-7 h-7 rounded-lg bg-blue-100 flex items-center justify-center text-sm">
                🩺
              </span>
              <div>
                <span className="serif font-bold text-ink text-sm">{caseInfo.title}</span>
                <span className="text-ink-light/50 text-xs ml-3">
                  {caseInfo.patient_profile.name} · {caseInfo.patient_profile.age}岁 · {caseInfo.patient_profile.gender}
                </span>
              </div>
            </div>
          </>
        )}
        <div className="ml-auto flex items-center gap-3">
          {sessionStatus === 'in_progress' && (
            <button
              onClick={() => setShowEndConfirm(true)}
              className="px-4 py-1.5 rounded-xl text-sm font-medium bg-red-50 text-red-600 border border-red-200 hover:bg-red-100 transition-all cursor-pointer"
            >
              结束问诊
            </button>
          )}
          <span className={`text-xs px-2.5 py-1 rounded-full font-medium ${
            sessionStatus === 'in_progress'
              ? 'bg-emerald-100 text-emerald-700'
              : 'bg-gray-100 text-ink-light/60'
          }`}>
            {sessionStatus === 'in_progress' ? '进行中' : '已结束'}
          </span>
        </div>
      </div>

      {/* Chat area */}
      <div ref={containerRef} className="flex-1 overflow-y-auto bg-gradient-to-b from-slate-50 to-gray-50">
        <ChatContainer messages={messages} isLoading={isLoading} caseInfo={caseInfo} />
      </div>

      {/* Input area */}
      {sessionStatus === 'in_progress' && (
        <ChatInput onSend={handleSend} disabled={isLoading} />
      )}

      {sessionStatus === 'completed' && (
        <div className="bg-white/80 backdrop-blur-md border-t border-gray-100 px-4 py-4 text-center">
          <p className="text-ink font-semibold mb-1">问诊已结束</p>
          <p className="text-ink-light/60 text-sm mb-4">AI 考官已准备好为你生成 OSCE 评估报告</p>
          {currentSessionId && (
            <button
              onClick={() => navigate(`/evaluation/${currentSessionId}`)}
              className="px-6 py-2.5 bg-primary text-white rounded-2xl hover:bg-primary-dark transition-all cursor-pointer font-semibold shadow-sm hover:shadow-md hover:shadow-primary/20"
            >
              查看评估报告 →
            </button>
          )}
        </div>
      )}

      {/* End confirmation modal */}
      {showEndConfirm && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm flex items-center justify-center z-50 animate-fade-in" onClick={() => setShowEndConfirm(false)}>
          <div className="bg-white rounded-2xl p-7 max-w-sm mx-4 shadow-2xl animate-scale-in" onClick={(e) => e.stopPropagation()}>
            <div className="text-center mb-4">
              <span className="text-4xl">📝</span>
            </div>
            <h3 className="serif text-xl font-bold text-ink text-center mb-2">结束问诊？</h3>
            <p className="text-ink-light text-sm text-center mb-6 leading-relaxed">
              结束后 AI 考官将自动分析对话记录，生成包含四维 OSCE 评分和详细反馈的评估报告。
            </p>
            <div className="flex gap-3">
              <button
                onClick={() => setShowEndConfirm(false)}
                className="flex-1 px-4 py-2.5 rounded-xl text-ink-light border border-gray-200 hover:bg-gray-50 transition-colors cursor-pointer font-medium"
              >
                继续问诊
              </button>
              <button
                onClick={handleEndSession}
                className="flex-1 px-4 py-2.5 rounded-xl bg-primary text-white hover:bg-primary-dark transition-all cursor-pointer font-semibold shadow-sm"
              >
                确认结束
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
