import React from 'react';
import { useNavigate } from 'react-router-dom';

const SearchResultItem = ({ result }) => {
  const navigate = useNavigate();

  const handleViewDocument = () => {
    navigate(`/document/${result.id}`);
  };

  return (
    <div className="search-result-item">
      <div className="result-header">
        <h4>{result.title}</h4>
        <button className="view-document-btn" onClick={handleViewDocument}>
          詳細表示
        </button>
      </div>
      
      <div className="result-meta">
        <span className="authors">{result.authors.join(', ')}</span>
        <span className="date">{result.publicationDate}</span>
        <span className="citations">被引用数: {result.citations}</span>
        <span className="journal">{result.journal}</span>
      </div>
      
      <div className="result-abstract">
        <p>{result.abstract}</p>
      </div>
      
      <div className="result-evaluation">
        <div className="evaluation-score">
          <strong>評価スコア: </strong>
          {result.score}
        </div>
        <div className="evaluation-reason">
          <strong>評価理由: </strong>
          {result.evaluationReason}
        </div>
      </div>
    </div>
  );
};

export default SearchResultItem;