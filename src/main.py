# src/main.py
"""
論文整理アプリケーションのメインエントリーポイント
"""

from flask import Flask
from src.api.routes import api_bp

def create_app():
    """Flaskアプリケーションを作成する"""
    app = Flask(__name__)
    
    # ルートを登録
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)