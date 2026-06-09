export interface CaseItem {
  id: string
  title: string
  department: string
  difficulty: 'beginner' | 'intermediate' | 'advanced'
  chief_complaint: string
  patient_profile: PatientProfile
  is_active: boolean
}

export interface PatientProfile {
  name: string
  age: number
  gender: string
  occupation: string
}

export interface CaseDetail extends CaseItem {
  symptoms_description: string
  physical_exam: Record<string, string>
  emotional_state: string
  key_questions: string[]
  red_flags: string[]
}

export interface Session {
  id: string
  case_id: string
  case_title?: string
  status: 'in_progress' | 'completed' | 'abandoned'
  started_at: string
  completed_at: string | null
  messages?: Message[]
}

export interface Message {
  id: string
  session_id: string
  role: 'student' | 'patient' | 'system'
  content: string
  timestamp: string
}

export interface Evaluation {
  id: string
  session_id: string
  overall_score: number
  dimensions: {
    completeness: DimensionScore
    communication: DimensionScore
    clinical_thinking: DimensionScore
    objective: ObjectiveScore
  }
  summary: string
  diagnosis_guess: string
  created_at: string
}

export interface DimensionScore {
  score: number
  strengths: string[]
  improvements: string[]
  feedback: string
}

export interface ObjectiveScore extends DimensionScore {
  items_covered: number
  items_total: number
  covered_list: string[]
  missed_list: string[]
}
