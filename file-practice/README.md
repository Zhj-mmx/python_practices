# 🐍 Python 文件操作练习

**位置**：`D:\Python_code\file-practice\`

---

## 📁 目录结构

```
D:\Python_code\
├── file-practice/           # 文件操作练习
│   ├── 01_hello_file.py     # 写入文件
│   ├── 02_read_file.py      # 读取文件（3 种方式）
│   ├── 03_append_mode.py    # 追加模式
│   ├── 04_with_statement.py # with 语句（最佳实践）
│   ├── 05_file_info.py      # os/pathlib 模块
│   ├── 06_batch_processor.py# 批量处理
│   ├── data/                # 数据文件夹
│   └── README.md
├── week1/                   # 第一周基础
├── projects/                # 项目代码
└── ...
```

---

## 🚀 运行练习

### 方式 1：VS Code 运行
1. 打开 `D:\Python_code\file-practice\`
2. 右键 `.py` 文件 → `Run Python File`

### 方式 2：终端运行
```bash
cd D:\Python_code\file-practice
python 01_hello_file.py
python 02_read_file.py
# ... 依次运行
```

### 方式 3：Code Runner 扩展
- 按 `Ctrl + Alt + N` 运行当前文件

---

## 📋 练习清单

| 练习 | 文件 | 核心技能 | 难度 |
|------|------|----------|------|
| 1 | `01_hello_file.py` | `open()`, `write()`, `close()` | 🟢 |
| 2 | `02_read_file.py` | `read()`, `readlines()`, 迭代 | 🟢 |
| 3 | `03_append_mode.py` | 追加模式 `"a"` | 🟢 |
| 4 | `04_with_statement.py` | `with` 语句 | 🟡 |
| 5 | `05_file_info.py` | `os`, `pathlib` | 🟡 |
| 6 | `06_batch_processor.py` | 批量处理 | 🟠 |

---

## 📚 文件模式速查

| 模式 | 含义 | 文件不存在 | 文件存在 |
|------|------|-----------|----------|
| `"r"` | 读取 | 报错 | 从头读取 |
| `"w"` | 写入 | 创建 | **清空覆盖** |
| `"a"` | 追加 | 创建 | 从末尾追加 |
| `"r+"` | 读写 | 报错 | 从头读写 |
| `"rb"` | 二进制读取 | 报错 | 读取二进制 |

---

## 💡 最佳实践

### ✅ 推荐：with 语句
```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
# 自动关闭，安全
```

### ❌ 不推荐：手动 close
```python
f = open("file.txt", "r")
content = f.read()
f.close()  # 容易忘记！
```

---

## 🎯 进阶挑战

### 挑战 1：日记本程序
```python
# 让用户输入日记，保存到 data/diary/2026-03-27.txt
```

### 挑战 2：文件备份工具
```python
# 把 data/ 下所有 .txt 复制为 .bak 后缀
```

### 挑战 3：日志分析器
```python
# 统计日志文件中包含 "ERROR" 的行数
```

### 挑战 4：CSV 数据读取（为课题组准备）
```python
# 读取小鼠实验数据 CSV
# 解析成字典/列表
```

---

**加油，梦哥！🐍**
