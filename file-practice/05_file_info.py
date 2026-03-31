# 05_file_info.py
# 目标：学会使用 os 和 pathlib 模块

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
from pathlib import Path

filename = "data/greeting.txt"

# 方式 1：使用 os 模块
print("=== os 模块 ===")
print(f"文件存在：{os.path.exists(filename)}") #exists
print(f"文件大小：{os.path.getsize(filename)} 字节") #getsize
print(f"绝对路径：{os.path.abspath(filename)}") #abspath
print(f"文件名：{os.path.basename(filename)}") #basename
print(f"目录名：{os.path.dirname(filename)}") #filename

# 方式 2：使用 pathlib（更现代，推荐）
print("\n=== pathlib 模块 ===")
path = Path(filename)
print(f"文件存在：{path.exists()}")
print(f"文件大小：{path.stat().st_size} 字节")
print(f"绝对路径：{path.resolve()}")
print(f"文件名：{path.name}")
print(f"后缀名：{path.suffix}")
print(f"不含后缀：{path.stem}")

# 创建目录
os.makedirs("data/subfolder", exist_ok=True)
print("\n[OK] 已创建目录：data/subfolder")
