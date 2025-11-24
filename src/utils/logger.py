# src/utils/logger.py
"""
ロガー設定
"""

from loguru import logger
import sys

# ロガー設定
logger.remove()  # 既存のハンドラを削除
logger.add(sys.stdout, level="INFO")  # 標準出力にINFOレベル以上を出力
logger.add("logs/app.log", rotation="500 MB", level="DEBUG")  # ファイルにDEBUGレベル以上を出力

# ロガーを返す
def get_logger():
    return logger