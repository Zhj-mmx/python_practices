# Python 文件操作完整练习
# 作者：Dreamclaw
# 日期：2026-03-31

import os
import json
import csv
from pathlib import Path

# ============================================
# 第一部分：基础文件操作
# ============================================

def practice_basic_write():
    """练习 1：写入文件"""
    print("【练习 1】写入文件")
    
    # 方法 1：with 语句（推荐）
    with open('test_write.txt', 'w', encoding='utf-8') as f:
        f.write("第一行：你好，文件操作！\n")
        f.write("第二行：这是 Python 写入的内容\n")
        f.write("第三行：支持中文\n")
    
    # 方法 2：追加模式
    with open('test_write.txt', 'a', encoding='utf-8') as f:
        f.write("第四行：追加的内容\n")
    
    print("✓ 写入完成，查看 test_write.txt\n")


def practice_basic_read():
    """练习 2：读取文件"""
    print("【练习 2】读取文件")
    
    # 方法 1：read() - 读取全部
    with open('test_write.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print("read() 全部内容：")
        print(content)
    
    # 方法 2：readline() - 逐行读取
    print("readline() 逐行读取：")
    with open('test_write.txt', 'r', encoding='utf-8') as f:
        line1 = f.readline()
        line2 = f.readline()
        print(f"第 1 行：{line1.strip()}")
        print(f"第 2 行：{line2.strip()}")
    
    # 方法 3：readlines() - 读取为列表
    with open('test_write.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"\nreadlines() 共 {len(lines)} 行")
        for i, line in enumerate(lines, 1):
            print(f"  行{i}: {line.strip()}")
    
    # 方法 4：直接迭代（最 Pythonic）
    print("\n直接迭代文件对象：")
    with open('test_write.txt', 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            print(f"  行{line_num}: {line.strip()}")
    
    print("\n✓ 读取练习完成\n")


def practice_file_copy():
    """练习 3：文件复制"""
    print("【练习 3】文件复制")
    
    # 读取源文件，写入新文件
    with open('test_write.txt', 'r', encoding='utf-8') as src:
        content = src.read()
    
    with open('test_copy.txt', 'w', encoding='utf-8') as dst:
        dst.write("=== 复制的文件 ===\n")
        dst.write(content)
    
    print("✓ 文件已复制到 test_copy.txt\n")


# ============================================
# 第二部分：路径处理 (pathlib)
# ============================================

def practice_pathlib():
    """练习 4：使用 pathlib 处理路径"""
    print("【练习 4】pathlib 路径操作")
    
    # 创建路径对象
    current_dir = Path('.')
    print(f"当前目录：{current_dir.absolute()}")
    
    # 拼接路径（跨平台兼容）
    test_file = current_dir / 'test_write.txt'
    print(f"文件路径：{test_file}")
    print(f"文件存在：{test_file.exists()}")
    print(f"是文件：{test_file.is_file()}")
    print(f"文件名：{test_file.name}")
    print(f"文件后缀：{test_file.suffix}")
    print(f"父目录：{test_file.parent}")
    
    # 创建目录
    new_dir = current_dir / 'practice_data'
    new_dir.mkdir(exist_ok=True)
    print(f"\n✓ 创建目录：{new_dir.absolute()}")
    
    # 列出目录下所有文件
    print("\n当前目录文件：")
    for item in current_dir.iterdir():
        if item.is_file() and item.suffix == '.txt':
            print(f"  📄 {item.name}")
    
    print()


# ============================================
# 第三部分：CSV 文件操作
# ============================================

def practice_csv():
    """练习 5：CSV 文件读写"""
    print("【练习 5】CSV 文件操作")
    
    # 写入 CSV
    data = [
        ['姓名', '年龄', '城市'],
        ['张三', 25, '北京'],
        ['李四', 30, '上海'],
        ['王五', 28, '广州'],
    ]
    
    with open('data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("✓ CSV 写入完成")
    
    # 读取 CSV
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print("\n读取 CSV 内容：")
        for row in reader:
            print(f"  {row}")
    
    # 使用 DictWriter/DictReader
    print("\n使用字典方式写入 CSV：")
    students = [
        {'name': '小明', 'score': 95},
        {'name': '小红', 'score': 88},
        {'name': '小刚', 'score': 92},
    ]
    
    with open('students.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['name', 'score']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    
    with open('students.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("读取学生数据：")
        for row in reader:
            print(f"  {row['name']}: {row['score']}分")
    
    print("\n✓ CSV 练习完成\n")


# ============================================
# 第四部分：JSON 文件操作
# ============================================

def practice_json():
    """练习 6：JSON 文件读写"""
    print("【练习 6】JSON 文件操作")
    
    # Python 数据结构
    data = {
        'name': '梦哥',
        'university': '南昌大学',
        'major': '人工智能',
        'interests': ['AI', '数据结构', 'Python'],
        'courses': [
            {'name': '数据结构', 'grade': 90},
            {'name': 'Python 编程', 'grade': 95},
        ]
    }
    
    # 写入 JSON
    with open('profile.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✓ JSON 写入完成")
    
    # 读取 JSON
    with open('profile.json', 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
        print(f"\n读取 JSON：{loaded_data['name']} - {loaded_data['university']}")
        print(f"兴趣：{', '.join(loaded_data['interests'])}")
    
    # 格式化输出
    print("\n格式化 JSON：")
    print(json.dumps(data, ensure_ascii=False, indent=2))
    
    print("\n✓ JSON 练习完成\n")


# ============================================
# 第五部分：二进制文件操作
# ============================================

def practice_binary():
    """练习 7：二进制文件操作"""
    print("【练习 7】二进制文件操作")
    
    # 写入二进制数据
    data = bytes([65, 66, 67, 68, 69])  # ABCDE
    with open('binary.dat', 'wb') as f:
        f.write(data)
    print("✓ 二进制写入完成")
    
    # 读取二进制数据
    with open('binary.dat', 'rb') as f:
        content = f.read()
        print(f"读取内容：{content}")
        print(f"解码后：{content.decode('ascii')}")
    
    # 复制图片（示例）
    print("\n提示：复制图片/视频用同样的方法，只是文件更大")
    print("  with open('source.jpg', 'rb') as src:")
    print("      with open('copy.jpg', 'wb') as dst:")
    print("          dst.write(src.read())")
    
    print("\n✓ 二进制练习完成\n")


# ============================================
# 第六部分：综合练习
# ============================================

def practice_log_system():
    """练习 8：实现简单日志系统"""
    print("【练习 8】简易日志系统")
    
    log_file = Path('app.log')
    
    # 追加日志
    import datetime
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] 程序运行正常\n")
        f.write(f"[{timestamp}] 文件操作练习完成\n")
    
    print("✓ 日志已写入 app.log")
    
    # 读取最新 5 条日志
    if log_file.exists():
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"\n最新日志（共{len(lines)}条）：")
            for line in lines[-5:]:
                print(f"  {line.strip()}")
    
    print()


def cleanup():
    """清理练习文件"""
    print("【清理】删除练习文件")
    files_to_delete = [
        'test_write.txt', 'test_copy.txt', 'data.csv', 
        'students.csv', 'profile.json', 'binary.dat', 'app.log'
    ]
    
    for filename in files_to_delete:
        path = Path(filename)
        if path.exists():
            path.unlink()
            print(f"  ✓ 删除 {filename}")
    
    # 删除目录
    practice_dir = Path('practice_data')
    if practice_dir.exists():
        practice_dir.rmdir()
        print(f"  ✓ 删除目录 {practice_dir}")
    
    print()


# ============================================
# 主程序
# ============================================

if __name__ == '__main__':
    print("=" * 50)
    print("Python 文件操作完整练习")
    print("=" * 50)
    print()
    
    # 执行所有练习
    practice_basic_write()
    practice_basic_read()
    practice_file_copy()
    practice_pathlib()
    practice_csv()
    practice_json()
    practice_binary()
    practice_log_system()
    
    print("=" * 50)
    print("所有练习完成！🎉")
    print("=" * 50)
    
    # 询问是否清理
    choice = input("\n是否删除练习文件？(y/n): ")
    if choice.lower() == 'y':
        cleanup()
        print("清理完成！")
    else:
        print("练习文件已保留，可以手动查看")
