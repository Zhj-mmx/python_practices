import sys 
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

filename = 'data/greeting.txt'

file = open(filename, "w", encoding="utf-8")
file.write("Hello, Python File!\n") #\n 做换行符
file.write("你好，文件操作\n")
file.close()

