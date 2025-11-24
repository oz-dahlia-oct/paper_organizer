import React, { useState } from 'react';

const SearchForm = ({ onSearch }) => {
  const [theme, setTheme] = useState('');
  const [priorityScores, setPriorityScores] = useState(['影響力', '新規性', '実用性']);
  const [searchSettings, setSearchSettings] = useState({
    timeRange: '1年',
    maxResults: 20
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    const searchData = {
      theme,
      priorityScores,
      searchSettings
    };
    onSearch(searchData);
  };

  return (
    <form className="search-form" onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="theme">テーマ</label>
        <input
          type="text"
          id="theme"
          value={theme}
          onChange={(e) => setTheme(e.target.value)}
          placeholder="検索するテーマを入力"
          required
        />
      </div>

      <div className="form-group">
        <label>優先順位スコア項目</label>
        <div className="score-items">
          {priorityScores.map((score, index) => (
            <div key={index} className="score-item">
              <input
                type="text"
                value={score}
                onChange={(e) => {
                  const newScores = [...priorityScores];
                  newScores[index] = e.target.value;
                  setPriorityScores(newScores);
                }}
                placeholder="スコア項目"
              />
              <button type="button" onClick={() => {
                const newScores = [...priorityScores];
                newScores.splice(index, 1);
                setPriorityScores(newScores);
              }}>
                削除
              </button>
            </div>
          ))}
          <button
            type="button"
            onClick={() => setPriorityScores([...priorityScores, ''])}
            className="add-score-btn"
          >
            スコア項目を追加
          </button>
        </div>
      </div>

      <div className="form-group">
        <label htmlFor="timeRange">検索期間</label>
        <select
          id="timeRange"
          value={searchSettings.timeRange}
          onChange={(e) => setSearchSettings({...searchSettings, timeRange: e.target.value})}
        >
          <option value="1年">過去1年</option>
          <option value="3年">過去3年</option>
          <option value="5年">過去5年</option>
          <option value="10年">過去10年</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="maxResults">最大結果数</label>
        <input
          type="number"
          id="maxResults"
          value={searchSettings.maxResults}
          onChange={(e) => setSearchSettings({...searchSettings, maxResults: parseInt(e.target.value)})}
          min="1"
          max="100"
        />
      </div>

      <button type="submit" className="search-submit-btn">
        検索
      </button>
    </form>
  );
};

export default SearchForm;