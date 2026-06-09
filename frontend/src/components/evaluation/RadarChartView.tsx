import {
  Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer,
} from 'recharts'

interface Props {
  completeness: number
  communication: number
  clinicalThinking: number
  objective: number
}

export default function RadarChartView({ completeness, communication, clinicalThinking, objective }: Props) {
  const data = [
    { dimension: '问诊完整性', score: completeness, full: 100 },
    { dimension: '医患沟通', score: communication, full: 100 },
    { dimension: '临床思维', score: clinicalThinking, full: 100 },
    { dimension: '客观评分', score: objective, full: 100 },
  ]

  return (
    <div className="bg-white rounded-xl p-6 border border-paper-dark">
      <h3 className="serif text-lg font-bold text-ink mb-4">四维评估雷达图</h3>
      <ResponsiveContainer width="100%" height={320}>
        <RadarChart data={data} cx="50%" cy="50%" outerRadius="75%">
          <PolarGrid stroke="#e5e7eb" />
          <PolarAngleAxis
            dataKey="dimension"
            tick={{ fontSize: 13, fill: '#374151', fontFamily: 'Noto Serif SC, serif' }}
          />
          <PolarRadiusAxis
            angle={90}
            domain={[0, 100]}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickCount={5}
          />
          <Radar
            name="评分"
            dataKey="score"
            stroke="#1a73e8"
            fill="#1a73e8"
            fillOpacity={0.15}
            strokeWidth={2}
          />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  )
}
