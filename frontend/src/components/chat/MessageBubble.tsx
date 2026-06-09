import type { Message } from '../../types'

interface Props {
  message: Message
}

function formatTime(iso: string) {
  if (!iso) return ''
  const d = new Date(iso)
  return `${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')}`
}

export default function MessageBubble({ message }: Props) {
  const isStudent = message.role === 'student'
  const timestamp = formatTime(message.timestamp)

  return (
    <div className={`flex ${isStudent ? 'justify-end' : 'justify-start'} mb-4 animate-fade-in-up`}>
      {/* Patient avatar */}
      {!isStudent && (
        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-medical to-primary flex items-center justify-center text-white text-xs font-bold shrink-0 mr-2.5 mt-1 shadow-sm">
          AI
        </div>
      )}

      <div className="flex flex-col max-w-[70%]">
        {!isStudent && (
          <span className="text-xs text-ink-light/60 mb-1 ml-1 font-medium">
            AI 标准化病人
          </span>
        )}

        <div
          className={`px-4 py-2.5 text-[15px] leading-relaxed whitespace-pre-wrap ${
            isStudent
              ? 'bg-primary text-white rounded-2xl rounded-br-md shadow-sm'
              : 'bg-white text-ink rounded-2xl rounded-bl-md shadow-sm border border-gray-100'
          }`}
        >
          {message.content}
        </div>

        {timestamp && (
          <span className={`text-xs text-ink-light/40 mt-1 ${isStudent ? 'text-right mr-1' : 'ml-1'}`}>
            {timestamp}
          </span>
        )}
      </div>

      {/* Student avatar */}
      {isStudent && (
        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-slate-500 to-slate-600 flex items-center justify-center text-white text-xs font-bold shrink-0 ml-2.5 mt-1 shadow-sm">
          我
        </div>
      )}
    </div>
  )
}
