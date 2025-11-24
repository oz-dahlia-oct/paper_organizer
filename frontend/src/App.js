import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import SearchPage from './pages/SearchPage';
import EvaluationPage from './pages/EvaluationPage';
import DocumentPage from './pages/DocumentPage';
import './styles/global.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/evaluation" element={<EvaluationPage />} />
          <Route path="/document/:id" element={<DocumentPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;