# src/models/document.py
"""
文書モデル定義
"""

from pydantic import BaseModel
from typing import List, Optional

class Content(BaseModel):
    """コンテンツモデル"""
    content_type: str  # image, markdown, mathjax
    content: str
    language: Optional[str] = None
    translations: Optional[List[dict]] = None

class Document(BaseModel):
    """文書モデル"""
    document_id: str
    page: int
    contents: List[Content]