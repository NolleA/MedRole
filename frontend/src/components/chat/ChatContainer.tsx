import type { Message, CaseDetail } from '../../types'
import MessageBubble from './MessageBubble'

interface Props {
  messages: Message[]
  isLoading: boolean
  caseInfo: CaseDetail | null
}

export default function ChatContainer({ messages, isLoading, caseInfo }: Props) {
  return (
    <div className="max-w-4xl mx-auto px-4 py-4">
      {messages.length === 0 && !isLoading ? (
        <div className="flex flex-col items-center justify-center min-h-[300px] text-center">
          <div className="w-16 h-16 bg-gradient-to-br from-blue-100 to-cyan-100 rounded-2xl flex items-center justify-center text-3xl mb-4 shadow-sm">
            🩺
          </div>
          <p className="text-ink font-semibold text-lg mb-1">准备开始问诊</p>
          <p className="text-ink-light text-sm">
            {caseInfo
              ? `当前病例：${caseInfo.title} — ${caseInfo.chief_complaint}`
              : 'AI 标准化病人已就位，请在下方输入你的第一个问题'}
          </p>
        </div>
      ) : (
        <>
          {messages.map((msg) => (
            <MessageBubble key={msg.id} message={msg} />
          ))}

          {isLoading && (
            <div className="flex justify-start mb-4 animate-fade-in">
              <div className="w-8 h-8 rounded-full bg-gradient-to-br from-medical to-primary flex items-center justify-center text-white text-xs font-bold shrink-0 mr-2.5 mt-1 shadow-sm">
                AI
              </div>
              <div className="flex flex-col max-w-[70%]">
                <span className="text-xs text-ink-light/60 mb-1 ml-1 font-medium">AI 标准化病人</span>
                <div className="bg-white rounded-2xl rounded-bl-md px-4 py-3 shadow-sm border border-gray-100">
                  <div className="flex gap-1.5">
                    <span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                    <span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                    <span className="w-2 h-2 bg-slate-300 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                  </div>
                </div>
              </div>
            </div>
          )}
        </>
      )}
    </div>
  )
}
