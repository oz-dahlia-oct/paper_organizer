# tests/test_evaluation_service.py
"""
評価サービスのテスト
"""

import pytest
from src.services.evaluation_service import evaluate_papers

def test_evaluate_papers():
    """論文評価のテスト"""
    papers = [
        {
            "title": "Example Paper 1",
            "authors": ["Author A", "Author B"],
            "publication_date": "2023-01-01",
            "citation_count": 10,
            "journal": "Journal of Example",
            "abstract": "This is an example abstract.",
            "abstract_translations": [
                {
                    "language": "japanese",
                    "content": "これは例の要旨です。"
                }
            ]
        }
    ]
    priority_scores = ["relevance", "impact"]
    
    result = evaluate_papers(papers, priority_scores)
    
    # ここに適切なアサーションを追加
    assert isinstance(result, list)