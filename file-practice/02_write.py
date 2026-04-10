import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding= 'utf-8')

filename = "data/greeting.txt"

file = open(filename, "r", encoding='utf-8')
content = file.read()
print("方式 1 - 全部读取：")
print(content)

lines = file.readlines()
print("方式 2 - 按行读取：")
for i, line in enumerate(lines, 1):
    print(f"第{i}行：{line.strip()}")
file.close()

print("方式 3 - 逐行迭代：")
file = open(filename, "r", encoding='utf-8')
for line in file:
    print(f" - {line.strip()}")
file.close()
