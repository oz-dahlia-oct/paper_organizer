# src/models/document.py
"""
文書モデル定義
"""

from pydantic import BaseModel, RootModel, ConfigDict, Field
from typing import List, Dict, Optional, Annotated


class SubElement(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: Annotated[
        str,
        Field(..., description="副要素の名称"),
    ]
    reason: Annotated[
        str,
        Field(..., description="なぜその副要素がテーマと関連するのかの理由"),
    ]
    description: Annotated[
        str,
        Field(..., description="副要素の詳細に関する説明"),
    ]


class Element(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: Annotated[
        str,
        Field(..., description="副要素の名称"),
    ]
    reason: Annotated[
        str,
        Field(..., description="なぜその副要素がテーマと関連するのかの理由"),
    ]
    description: Annotated[
        str,
        Field(..., description="副要素の詳細に関する説明"),
    ]
    sub_elements: Annotated[
        List[SubElement],
        Field(..., description="副要素のリスト"),
    ]


class Elements(BaseModel):
    model_config = ConfigDict(extra="forbid")
    elements: Annotated[
        List[Element],
        Field(..., description="テーマに関連する要素のリスト"),
    ]


class TranslatedPaper(BaseModel):
    """1件分の論文翻訳情報"""

    title_ja: Annotated[
        str,
        Field(
            ...,
            description="論文タイトルの日本語訳",
        ),
    ]
    summary_ja: Annotated[
        str,
        Field(
            description="論文の要約テキストの日本語訳",
        ),
    ]

class TranslatedPapers(RootModel):
    """論文 ID -> Paper のマッピング全体"""

    root: Annotated[
        Dict[str, TranslatedPaper],
        Field(
            description=(
                "数値 ID（'0', '1', '2', ...）を論文IDとし、値として論文の翻訳情報を持つマップ。"
            ),
            examples=[
                {
                    0: {
                        "title_ja": "三つのバブルとパニック：最近の食料一次産品価格の動向に関する解説的レビュー",
                        "summary_ja": "…米ドルの減価に対する反応は、牛肉でおよそ 0.9、トウモロコシで 0.35 の範囲であり、コメ、小麦、油糧種子はいずれも 0.5 未満である。また、食料価格の変化は……と強い相関を示していない。",
                    }
                }
            ],
        ),
    ]


class Theme(BaseModel):
    pass


class Content(BaseModel):
    """コンテンツモデル"""

    content_type: str
    content: str
    language: Optional[str] = None
    translations: Optional[List[dict]] = None


class Document(BaseModel):
    """文書モデル"""

    document_id: str
    page: int
    contents: List[Content]
