import os
import json
import csv
from pathlib import Path

def practice_basic_write():
    with open('test_write.txt', 'w', encoding = 'utf-8') as f:
        f.write("这是写入文件的第一行\n")
        f.write("用来测试write写入很多行的情况，这句话用来填充，这句话用来填充，这句话用来填充，这句话用来填充\n")
        f.writelines(这是writelines的效果\n")

    with open('test_write.txt', 'a', encoding = 'utf-8') as f:
        f.write("这是追加的文件部分\n")

    print("写入文件完成")



if __name__ == '__main__':
    practice_basic_write()

