import { useEffect, useState } from 'react'
import { api } from '../api/client'
import CaseCard from '../components/cases/CaseCard'
import CaseFilter from '../components/cases/CaseFilter'
import type { CaseItem } from '../types'

export default function CaseListPage() {
  const [cases, setCases] = useState<CaseItem[]>([])
  const [loading, setLoading] = useState(true)
  const [department, setDepartment] = useState('')
  const [difficulty, setDifficulty] = useState('')

  useEffect(() => {
    setLoading(true)
    const params = new URLSearchParams()
    if (department) params.set('department', department)
    if (difficulty) params.set('difficulty', difficulty)
    api.get<CaseItem[]>(`/cases?${params.toString()}`)
      .then(setCases)
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [department, difficulty])

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="flex items-baseline gap-4 mb-6">
        <h2 className="serif text-3xl font-bold text-ink">病例库</h2>
        <span className="text-sm text-gray-400">{cases.length} 个病例</span>
      </div>

      <CaseFilter
        department={department}
        difficulty={difficulty}
        onDepartmentChange={setDepartment}
        onDifficultyChange={setDifficulty}
      />

      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-6">
          {[...Array(3)].map((_, i) => (
            <div key={i} className="bg-white rounded-xl p-5 border border-paper-dark animate-pulse">
              <div className="h-4 bg-gray-200 rounded w-20 mb-3" />
              <div className="h-5 bg-gray-200 rounded w-3/4 mb-2" />
              <div className="h-4 bg-gray-100 rounded w-full mb-3" />
              <div className="h-3 bg-gray-100 rounded w-1/2" />
            </div>
          ))}
        </div>
      ) : cases.length === 0 ? (
        <div className="text-center py-16 text-gray-400">
          <p className="text-lg mb-2">没有匹配的病例</p>
          <p className="text-sm">请调整筛选条件</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-6">
          {cases.map((c) => (
            <CaseCard key={c.id} item={c} />
          ))}
        </div>
      )}
    </div>
  )
}
