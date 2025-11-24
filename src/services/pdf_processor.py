# src/services/pdf_processor.py
"""
PDF処理サービス
"""

import os
from pdf2image import convert_from_path
from PIL import Image
from src.models.document import Document

def process_pdf(pdf_path: str, output_dir: str) -> List[Document]:
    """
    PDFを処理し、画像化して文書モデルを返す
    
    Parameters:
        pdf_path (str): 入力PDFファイルパス
        output_dir (str): 出力ディレクトリパス
    
    Returns:
        List[Document]: 処理された文書リスト
    """
    # PDFを画像に変換
    images = convert_from_path(pdf_path, dpi=200)
    
    documents = []
    for i, image in enumerate(images):
        # 画像を保存
        image_path = os.path.join(output_dir, f"page_{i+1}.jpg")
        image.save(image_path, 'JPEG')
        
        # Documentモデルを作成
        document = Document(
            document_id=pdf_path,
            page=i+1,
            contents=[
                {
                    "content_type": "image",
                    "content": image_path
                }
            ]
        )
        documents.append(document)
    
    return documents