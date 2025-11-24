import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="header">
      <div className="header-container">
        <Link to="/" className="header-logo">
          研究テーマ検索
        </Link>
        <nav className="header-nav">
          <Link to="/" className="nav-link">ホーム</Link>
          <Link to="/search" className="nav-link">検索</Link>
          <Link to="/evaluation" className="nav-link">評価</Link>
        </nav>
      </div>
    </header>
  );
};

export default Header;