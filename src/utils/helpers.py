# src/utils/helpers.py
"""
ヘルパー関数
"""

import os
from datetime import datetime

def create_directories_if_not_exist(*dirs):
    """
    ディレクトリが存在しない場合に作成する
    
    Parameters:
        *dirs: ディレクトリパスの可変長引数
    """
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)

def get_current_timestamp():
    """
    現在のタイムスタンプを取得する
    
    Returns:
        str: ISOフォーマットのタイムスタンプ
    """
    return datetime.now().isoformat()