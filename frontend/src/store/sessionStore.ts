import { create } from 'zustand'
import { api } from '../api/client'
import type { Message, Session } from '../types'

interface SessionState {
  currentSessionId: string | null
  messages: Message[]
  isLoading: boolean
  sessionStatus: string | null

  startSession: (caseId: string) => Promise<string>
  sendMessage: (content: string) => Promise<void>
  endSession: () => Promise<void>
  loadSession: (sessionId: string) => Promise<void>
  resetSession: () => void
}

export const useSessionStore = create<SessionState>((set, get) => ({
  currentSessionId: null,
  messages: [],
  isLoading: false,
  sessionStatus: null,

  startSession: async (caseId: string) => {
    set({ isLoading: true, messages: [] })
    const session: Session = await api.post('/sessions', { case_id: caseId })
    set({
      currentSessionId: session.id,
      messages: session.messages || [],
      sessionStatus: session.status,
      isLoading: false,
    })
    return session.id
  },

  sendMessage: async (content: string) => {
    const { currentSessionId, messages } = get()
    if (!currentSessionId) return

    const tempId = `temp-${Date.now()}`
    const studentMsg: Message = {
      id: tempId,
      session_id: currentSessionId,
      role: 'student',
      content,
      timestamp: new Date().toISOString(),
    }

    set({ messages: [...messages, studentMsg], isLoading: true })

    try {
      const data = await api.post<{ student_message: Message; patient_message: Message }>(
        `/sessions/${currentSessionId}/chat`,
        { content }
      )
      set((state) => ({
        messages: [
          ...state.messages.filter((m) => m.id !== tempId),
          data.student_message,
          data.patient_message,
        ],
        isLoading: false,
      }))
    } catch {
      set((state) => ({
        messages: state.messages.map((m) =>
          m.id === tempId ? { ...m, id: m.id + '-failed' } : m
        ),
        isLoading: false,
      }))
    }
  },

  endSession: async () => {
    const { currentSessionId } = get()
    if (!currentSessionId) return
    await api.patch(`/sessions/${currentSessionId}`, { status: 'completed' })
    set({ sessionStatus: 'completed' })
  },

  loadSession: async (sessionId: string) => {
    set({ isLoading: true })
    const session: Session = await api.get(`/sessions/${sessionId}`)
    set({
      currentSessionId: session.id,
      messages: session.messages || [],
      sessionStatus: session.status,
      isLoading: false,
    })
  },

  resetSession: () => {
    set({
      currentSessionId: null,
      messages: [],
      isLoading: false,
      sessionStatus: null,
    })
  },
}))
