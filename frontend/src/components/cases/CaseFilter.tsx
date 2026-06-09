interface Props {
  department: string
  difficulty: string
  onDepartmentChange: (v: string) => void
  onDifficultyChange: (v: string) => void
}

const DEPTS = ['全部', '心内科', '神经内科', '呼吸内科', '消化内科', '风湿免疫科', '内分泌科', '骨科', '心胸外科', '妇产科']
const DIFFS = [
  { value: '', label: '全部' },
  { value: 'beginner', label: '初级' },
  { value: 'intermediate', label: '中级' },
  { value: 'advanced', label: '高级' },
]

export default function CaseFilter({ department, difficulty, onDepartmentChange, onDifficultyChange }: Props) {
  const btnClass = (active: boolean) =>
    `px-3.5 py-1.5 rounded-xl text-sm font-medium transition-all duration-200 cursor-pointer ${
      active
        ? 'bg-primary text-white shadow-sm shadow-primary/20'
        : 'bg-white text-ink-light hover:bg-gray-100 border border-gray-200 hover:border-gray-300'
    }`

  return (
    <div className="flex flex-wrap items-center gap-2.5">
      <span className="text-xs font-medium text-ink-light/60 uppercase tracking-wider">科室</span>
      {DEPTS.map((d) => (
        <button
          key={d}
          onClick={() => onDepartmentChange(d === '全部' ? '' : d)}
          className={btnClass((d === '全部' && !department) || department === d)}
        >
          {d}
        </button>
      ))}
      <span className="ml-2 text-xs font-medium text-ink-light/60 uppercase tracking-wider">难度</span>
      {DIFFS.map((d) => (
        <button
          key={d.value}
          onClick={() => onDifficultyChange(d.value)}
          className={btnClass(difficulty === d.value)}
        >
          {d.label}
        </button>
      ))}
    </div>
  )
}
