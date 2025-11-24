# tests/test_main.py
"""
メインアプリケーションのテスト
"""

import pytest
from src.main import create_app

def test_create_app():
    """アプリケーションの作成をテスト"""
    app = create_app()
    assert app is not None
    assert app.debug == True