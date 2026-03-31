# 02_read_file.py
# 目标：学会三种读取方式

import sys
import io
# 设置标准输出为 UTF-8，解决 Windows 终端乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filename = "data/greeting.txt"

# 方式 1：一次性读取全部内容read()
file = open(filename, "r", encoding="utf-8")
content = file.read()
print("方式 1 - 全部读取：")
print(content)
file.close()

# 方式 2：按行读取为列表readlines()
file = open(filename, "r", encoding="utf-8")
lines = file.readlines()
print("方式 2 - 按行读取：")
for i, line in enumerate(lines, 1):
    print(f"  第{i}行：{line.strip()}")
file.close()

# 方式 3：逐行迭代（推荐，省内存）
print("方式 3 - 逐行迭代：")
file = open(filename, "r", encoding="utf-8")
for line in file:
    print(f"  - {line.strip()}")
file.close()
