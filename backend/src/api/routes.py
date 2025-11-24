# src/api/routes.py
"""
APIルート定義
"""

from flask import Blueprint, jsonify, request
from src.services.search_service import search_papers
from src.services.evaluation_service import evaluate_papers

api_bp = Blueprint('api', __name__)

@api_bp.route('/search', methods=['POST'])
def search():
    """論文検索API"""
    data = request.get_json()
    theme = data.get('theme')
    priority_scores = data.get('priority_scores')
    search_settings = data.get('search_settings')
    
    papers = search_papers(theme, priority_scores, search_settings)
    return jsonify(papers)

@api_bp.route('/evaluate', methods=['POST'])
def evaluate():
    """論文評価API"""
    data = request.get_json()
    papers = data.get('papers')
    priority_scores = data.get('priority_scores')
    
    evaluated_papers = evaluate_papers(papers, priority_scores)
    return jsonify(evaluated_papers)