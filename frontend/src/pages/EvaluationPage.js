import React from 'react';
import Header from '../components/common/Header';

const EvaluationPage = () => {
  return (
    <div className="evaluation-page">
      <Header />
      <main className="evaluation-main">
        <div className="evaluation-container">
          <h2>論文評価</h2>
          <p>検索結果に基づいて、指定された優先順位スコア項目に基づいて評価します。</p>
          <div className="evaluation-content">
            <p>評価機能の実装中です。</p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default EvaluationPage;