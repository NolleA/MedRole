import { BrowserRouter, Routes, Route } from 'react-router-dom'
import AppLayout from './components/layout/AppLayout'
import HomePage from './pages/HomePage'
import CaseListPage from './pages/CaseListPage'
import ConsultationPage from './pages/ConsultationPage'
import EvaluationPage from './pages/EvaluationPage'
import HistoryPage from './pages/HistoryPage'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<AppLayout />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/cases" element={<CaseListPage />} />
          <Route path="/consultation/:sessionId" element={<ConsultationPage />} />
          <Route path="/evaluation/:sessionId" element={<EvaluationPage />} />
          <Route path="/history" element={<HistoryPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
