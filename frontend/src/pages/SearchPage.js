import React, { useState } from 'react';
import Header from '../components/common/Header';
import SearchForm from '../components/search/SearchForm';
import SearchResultList from '../components/search/SearchResultList';

const SearchPage = () => {
  const [searchResults, setSearchResults] = useState([]);
  const [isSearching, setIsSearching] = useState(false);

  const handleSearch = async (searchData) => {
    setIsSearching(true);
    // TODO: 実際のAPIコールをここに実装
    try {
      // 検索処理のシミュレーション
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // シミュレーションデータ
      const mockResults = [
        {
          id: '1',
          title: '生成AIによる創造性の解放',
          authors: ['山田太郎', '佐藤花子'],
          publicationDate: '2023-05-15',
          citations: 42,
          journal: '人工知能研究',
          abstract: '生成型AIは、かつて人間の心だけに属していた創造性を解き放っています。',
          score: 8.5,
          evaluationReason: 'AIによる創造性の解放についての新しい視点を提供'
        },
        {
          id: '2',
          title: 'マルチモーダルLLMの応用',
          authors: ['田中一郎', '鈴木二郎'],
          publicationDate: '2023-08-22',
          citations: 28,
          journal: '情報処理学会論文誌',
          abstract: 'マルチモーダルLLMを用いた新しい文書処理手法について検討した。',
          score: 7.2,
          evaluationReason: '実用的な応用例を示している'
        }
      ];
      
      setSearchResults(mockResults);
    } catch (error) {
      console.error('検索エラー:', error);
    } finally {
      setIsSearching(false);
    }
  };

  return (
    <div className="search-page">
      <Header />
      <main className="search-main">
        <div className="search-container">
          <h2>論文検索</h2>
          <SearchForm onSearch={handleSearch} />
          {isSearching && <div className="loading">検索中...</div>}
          <SearchResultList results={searchResults} />
        </div>
      </main>
    </div>
  );
};

export default SearchPage;