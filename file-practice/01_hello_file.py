# 01_hello_file.py
# 目标：学会使用 open() 和 write()

import sys
import io
# 设置标准输出为 UTF-8，解决 Windows 终端乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filename = "data/greeting.txt"

# 以写入模式打开（会覆盖原有内容）
file = open(filename, "w", encoding="utf-8")
file.write("Hello, Python File!\n")
file.write("你好，文件操作！\n")
file.close()

print(f"[OK] 文件已写入：{filename}")

"""
filename = "data/greeting.txt"

filen = open(filename, "w", encoding="utf-8")
file.write("Hello, Python File!\n")
file.close()
print(f"√ 文件已写入: {filename}")
""""