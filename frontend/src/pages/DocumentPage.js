import React from 'react';
import Header from '../components/common/Header';

const DocumentPage = () => {
  return (
    <div className="document-page">
      <Header />
      <main className="document-main">
        <div className="document-container">
          <h2>文書表示</h2>
          <p>PDF文書の内容を表示します。</p>
          <div className="document-content">
            <p>文書表示機能の実装中です。</p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DocumentPage;