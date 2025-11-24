# tests/test_search_service.py
"""
検索サービスのテスト
"""

import pytest
from src.services.search_service import search_papers

def test_search_papers():
    """論文検索のテスト"""
    theme = "example theme"
    priority_scores = ["relevance", "impact"]
    search_settings = {"year": "2023"}
    
    result = search_papers(theme, priority_scores, search_settings)
    
    # ここに適切なアサーションを追加
    assert isinstance(result, list)