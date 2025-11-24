# src/models/evaluation.py
"""
評価モデル定義
"""

from pydantic import BaseModel
from typing import List, Optional

class EvaluationScore(BaseModel):
    """評価スコア"""
    score_type: str
    score: float
    reason: str

class EvaluatedPaper(BaseModel):
    """評価された論文モデル"""
    title: str
    authors: List[str]
    publication_date: str
    citation_count: int
    journal: str
    abstract: str
    abstract_translations: Optional[List[dict]] = None
    scores: List[EvaluationScore]