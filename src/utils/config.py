# src/utils/config.py
"""
設定ファイル
"""

import os
from dotenv import load_dotenv

# 環境変数を読み込み
load_dotenv()

# Google Cloud 設定
GOOGLE_CLOUD_PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
GOOGLE_CLOUD_CREDENTIALS = os.getenv('GOOGLE_CLOUD_CREDENTIALS')

# PDF 処理設定
PDF_OUTPUT_DIR = os.getenv('PDF_OUTPUT_DIR', 'data/pdf_output')
IMAGE_OUTPUT_DIR = os.getenv('IMAGE_OUTPUT_DIR', 'data/image_output')

# LLM 設定
LLM_MODEL_NAME = os.getenv('LLM_MODEL_NAME', 'gpt-4')