import React from 'react';
import { useNavigate } from 'react-router-dom';
import Header from '../components/common/Header';

const HomePage = () => {
  const navigate = useNavigate();

  const handleStartSearch = () => {
    navigate('/search');
  };

  return (
    <div className="home-page">
      <Header />
      <main className="home-main">
        <div className="home-content">
          <h1>研究テーマ検索システム</h1>
          <p>テーマと優先順位スコア項目を指定して、関連する論文を検索・評価できます。</p>
          <button className="start-button" onClick={handleStartSearch}>
            検索を開始
          </button>
        </div>
      </main>
    </div>
  );
};

export default HomePage;