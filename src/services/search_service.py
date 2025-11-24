# src/services/search_service.py
"""
検索サービス
"""

from src.models.document import Document

def search_papers(theme: str, priority_scores: list, search_settings: dict) -> list:
    """
    論文を検索する
    
    Parameters:
        theme (str): 検索テーマ
        priority_scores (list): 優先順位スコア項目
        search_settings (dict): 検索設定
    
    Returns:
        list: 検索結果の論文リスト
    """
    # ここに検索ロジックを実装
    # 現在はダミーデータを返す
    return [
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