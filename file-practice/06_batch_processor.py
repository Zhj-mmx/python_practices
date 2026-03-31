# 06_batch_processor.py
# 目标：实际应用 - 批量处理文件

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
from pathlib import Path

# 创建一些测试文件
data_dir = Path("data")
for i in range(1, 6):
    with open(data_dir / f"note_{i}.txt", "w", encoding="utf-8") as f:
        f.write(f"这是第 {i} 个笔记文件\n")
        f.write(f"行号：{i}\n")

print("=== 批量读取文件 ===")

# 遍历目录
for file_path in data_dir.glob("*.txt"):
    print(f"\n[文件] {file_path.name}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)

# 统计文件数量
txt_files = list(data_dir.glob("*.txt"))
print(f"\n[OK] 共找到 {len(txt_files)} 个 txt 文件")

# 批量重命名（可选练习）
# for i, file_path in enumerate(data_dir.glob("note_*.txt"), 1):
#     new_name = f"renamed_{i}.txt"
#     file_path.rename(data_dir / new_name)
#     print(f"重命名：{file_path.name} → {new_name}")
