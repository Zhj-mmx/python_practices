# 03_append_mode.py
# 目标：学会追加模式，不覆盖原有内容

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filename = "data/greeting.txt"

# 以追加模式打开"a"
file = open(filename, "a", encoding="utf-8")
file.write("这是追加的第三行\n")
file.write("这是追加的第四行\n")
file.close()

# 读取验证
print("【追加后的内容】")
file = open(filename, "r", encoding="utf-8")
print(file.read())
file.close()
