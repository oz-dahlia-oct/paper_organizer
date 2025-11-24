# tests/test_pdf_processor.py
"""
PDF処理サービスのテスト
"""

import pytest
from src.services.pdf_processor import process_pdf

def test_process_pdf():
    """PDF処理のテスト"""
    # ダミーのPDFパスと出力ディレクトリを指定
    pdf_path = "dummy.pdf"
    output_dir = "dummy_output"
    
    # ダミーの処理結果を返す
    result = process_pdf(pdf_path, output_dir)
    
    # ここに適切なアサーションを追加
    assert isinstance(result, list)