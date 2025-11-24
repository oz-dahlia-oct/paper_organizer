# src/services/evaluation_service.py
"""
評価サービス
"""

from src.models.evaluation import EvaluatedPaper

def evaluate_papers(papers: list, priority_scores: list) -> list:
    """
    論文を評価する
    
    Parameters:
        papers (list): 論文リスト
        priority_scores (list): 優先順位スコア項目
    
    Returns:
        list: 評価された論文リスト
    """
    # ここに評価ロジックを実装
    # 現在はダミーデータを返す
    evaluated_papers = []
    for paper in papers:
        scores = []
        for score_type in priority_scores:
            scores.append({
                "score_type": score_type,
                "score": 5.0,  # ダミーのスコア
                "reason": f"評価理由: {score_type}"
            })
        
        evaluated_paper = EvaluatedPaper(
            title=paper["title"],
            authors=paper["authors"],
            publication_date=paper["publication_date"],
            citation_count=paper["citation_count"],
            journal=paper["journal"],
            abstract=paper["abstract"],
            abstract_translations=paper["abstract_translations"],
            scores=scores
        )
        evaluated_papers.append(evaluated_paper.dict())
    
    return evaluated_papers