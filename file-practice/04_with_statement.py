# 04_with_statement.py
# 目标：学会 Pythonic 的写法，自动关闭文件

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filename = "data/greeting.txt"

# 推荐写法：with 语句自动管理资源
print("使用 with 语句：")
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# 不需要 file.close()，with 块结束自动关闭

# 写入也可以用 with
with open("data/new_file.txt", "w", encoding="utf-8") as file:
    file.write("这是用 with 写入的文件\n")
    file.write("不用担心忘记 close()\n")

print("[OK] with 语句更安全，推荐使用！")

