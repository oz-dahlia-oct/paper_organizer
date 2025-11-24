import React from 'react';
import SearchResultItem from './SearchResultItem';

const SearchResultList = ({ results }) => {
  if (results.length === 0) {
    return <div className="no-results">検索結果がありません</div>;
  }

  return (
    <div className="search-results">
      <h3>検索結果 ({results.length} 件)</h3>
      <div className="results-list">
        {results.map((result) => (
          <SearchResultItem key={result.id} result={result} />
        ))}
      </div>
    </div>
  );
};

export default SearchResultList;