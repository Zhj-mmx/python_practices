好的，延续之前的风格，再为你准备一份 **《NumPy 基础操作进阶练习卷（5 题）》** 。每题依然披着“机器学习”的外衣，目的是让你熟悉更多常用函数。

---

## NumPy 基础操作进阶练习卷 (5题)

> 🧑‍🏫 **考前须知**：本卷假设你已经掌握了创建数组、索引切片、广播、基本聚合等操作。现在我们要解锁更多数据预处理中**高频使用**的技能：合并数据、统计描述、异常值处理、形状变换、类别统计。请先自己尝试填写代码，再翻看答案。

---

### 练习题 1：合并训练集与测试集 (vstack / hstack)

**场景故事：**
你手上有两份成绩数据——`train`（训练集，2 个学生的 3 科成绩）和 `test`（测试集，2 个学生的 3 科成绩）。在分析前，你想把**所有学生堆成一张大表**，就像把两个班级的名单上下拼接成一份全年级名单。

**任务要求：**
1. 将 `train` 和 `test` **上下堆叠**（行拼接），得到 `all_data`，形状应为 `(4, 3)`。
2. 假设又有了一个新特征列 `bonus`（加分）需要**左右拼接**到 `all_data` 的右侧，得到 `full_data`，形状应为 `(4, 4)`。

```python
import numpy as np

train = np.array([[78, 85, 90],
                  [65, 72, 88]])    # 学生A、B

test  = np.array([[92, 88, 95],
                  [55, 60, 70]])    # 学生C、D

bonus = np.array([[5],
                  [5],
                  [10],
                  [0]])             # 每个学生的额外加分

# ========== 你的代码在这里 ==========
all_data = None      # 提示：用 np.vstack 或者 np.concatenate
full_data = None     # 提示：用 np.hstack
# ===================================

print("合并后的全量数据 (4x3):\n", all_data)
print("加上加分列后 (4x4):\n", full_data)
print("full_data 形状:", full_data.shape)
```

<details>
<summary><b>✅ 点击查看答案与解析</b></summary>

```python
# 答案代码
all_data = np.vstack((train, test))     # 上下堆叠，就像两张纸粘在一起
full_data = np.hstack((all_data, bonus)) # 左右堆叠，在右边粘一列

print("合并后的全量数据 (4x3):\n", all_data)
print("加上加分列后 (4x4):\n", full_data)
print("full_data 形状:", full_data.shape)
```

**解析（初中生版）：**
- **vstack**：`v` 是 vertical（垂直，上下）。就像你把两张 A4 纸上下接起来，列数要完全一样。
- **hstack**：`h` 是 horizontal（水平，左右）。就像在成绩单最右边加一栏“附加分”，行数必须一样。
- 注意传给 vstack 和 hstack 的多个数组要用**元组**括起来，如 `(train, test)`。
</details>

---

### 练习题 2：数据统计描述 (mean, std, median, max, min)

**场景故事：**
拿到成绩表后，你想快速了解每门课的**平均分、波动程度（标准差）、中位数、最高分、最低分**。在机器学习中，这称为“描述性统计”，能帮你判断数据是否正常。

**任务要求：**
对 `scores` 数组（4个学生，3个科目），计算每科的上述五个统计量。**必须使用 axis 参数，一次性算出每科的结果。**

```python
scores = np.array([[78, 85, 90],
                   [65, 72, 88],
                   [92, 88, 95],
                   [55, 60, 70]])

# ========== 你的代码在这里 ==========
mean_score = None      # 每科平均分，axis=0 表示对列操作
std_score  = None      # 每科标准差
median_score = None    # 每科中位数
max_score  = None      # 每科最高分
min_score  = None      # 每科最低分
# ===================================

print("平均分:", mean_score)
print("标准差:", std_score)
print("中位数:", median_score)
print("最高分:", max_score)
print("最低分:", min_score)
```

<details>
<summary><b>✅ 点击查看答案与解析</b></summary>

```python
# 答案代码
mean_score = np.mean(scores, axis=0)      # axis=0 → 沿着行方向压缩，得到每列的统计值
std_score  = np.std(scores, axis=0)
median_score = np.median(scores, axis=0)
max_score  = np.max(scores, axis=0)
min_score  = np.min(scores, axis=0)

print("平均分:", mean_score)
print("标准差:", std_score)
print("中位数:", median_score)
print("最高分:", max_score)
print("最低分:", min_score)
```

**解析（初中生版）：**
- `axis=0` 可以想象成：**从天花板往下看，把每列的学生叠起来**，然后对这个“人堆”进行一次统计，得到每一科目的一个数字。
- **标准差**：衡量分数是不是“贫富差距很大”。标准差大，说明有人考 90 有人考 20。
- **中位数**：把所有分数从小到大排，正中间的那个数。不受极端值影响（比如有人考 0 分，平均分会拉低，但中位数可能还好）。
</details>

---

### 练习题 3：异常值检测与替换 (布尔索引 / np.where)

**场景故事：**
在真实数据中，传感器可能出错，导致收集到的温度数据出现离谱的值（比如 -999℃ 或 200℃）。你需要用 NumPy 把这种**明显的错误值**找出来，并替换成合理的数值（例如整列的平均值）。

**任务要求：**
`temps` 是 5 天里 3 个城市的温度记录。其中 -999 代表传感器故障。请：
1. 找出所有故障值的位置（用布尔索引）。
2. 把这些故障值替换为该**城市正常温度的均值**（即每列的非 -999 值的平均值）。

```python
temps = np.array([[ 25, -999,   30],
                  [ 27,   22,   33],
                  [-999,  21,   35],
                  [ 28,   20,  -999],
                  [ 26,   23,   31]])

# ========== 你的代码在这里 ==========
# 1. 先找故障位置 (布尔矩阵)
fault_mask = None          # 形状 = temps.shape，True 表示该点是 -999

# 2. 计算每列的正常均值（忽略 -999）
# 提示：可以先把 -999 变成 NaN 然后使用 np.nanmean，或者用掩码手动计算。
# 为了练习基础，尝试用掩码手动算：先复制 temps，把故障点暂时置0？不行，会拉低均值。
# 更好的办法：用掩码取出正常值，然后求平均。
# 但我们想要一个简单的方法：可以用 np.where 结合广播。
# 或：用 temps[~fault_mask] 得到所有正常值，但这会拉成一维，分不清列。
# 所以采用每列循环? 不行，要求向量化。我们可以这样：
# 把故障值替换成 0，然后求均值时除以正常值的个数。
# 方法一：用 np.where(mask, 0, temps) 然后求和，再除以 (~mask).sum(axis=0)
# 这里我们提供一个常见写法的填空：
normal_sum = np.where(fault_mask, 0, temps).sum(axis=0)  # 已给出提示，请补全
normal_count = None                                       # 正常值的个数
mean_normal = normal_sum / normal_count

# 3. 用 np.where 或直接布尔索引替换故障值
temps_cleaned = None       # 提示：用 np.where(fault_mask, 扩展mean_normal, temps)
# ===================================

print("故障掩码:\n", fault_mask)
print("每列正常均值:", mean_normal)
print("清洗后的温度:\n", temps_cleaned)
```

<details>
<summary><b>✅ 点击查看答案与解析</b></summary>

```python
# 答案代码
# 1. 故障掩码
fault_mask = (temps == -999)

# 2. 计算每列正常均值
normal_sum = np.where(fault_mask, 0, temps).sum(axis=0)   # 把故障置0，正常值求和
normal_count = (~fault_mask).sum(axis=0)                   # 正常值个数
mean_normal = normal_sum / normal_count

# 3. 替换：np.where(条件, 满足时用何值, 不满足时用原值)
# 需要把 mean_normal 广播成和 temps 一样的形状
temps_cleaned = np.where(fault_mask, mean_normal, temps)

print("故障掩码:\n", fault_mask)
print("每列正常均值:", mean_normal)
print("清洗后的温度:\n", temps_cleaned)
```

**解析（初中生版）：**
- `temps == -999` 直接对数组进行“等于判断”，返回一张全是 True/False 的表格（掩码）。
- **计算正常均值**：我们耍了个小聪明——把故障值先当成 0，然后加起来，再除以正常值的个数。因为加 0 不影响总和，所以和只加正常的数效果一样。
- `~fault_mask`：波浪号 `~` 是“取反”，把 True 变 False，False 变 True。
- **`np.where`**：就像 Excel 的 IF 函数。`np.where(条件是掩码, 是故障就用平均值, 否则用原来的温度)`。这里的 `mean_normal` 是 1 行 3 列，NumPy 会自动广播成 5 行 3 列来匹配。
</details>

---

### 练习题 4：图像数据形状变换 (reshape)

**场景故事：**
在图像识别中，一张图片通常是一个三维数组 `(高, 宽, 颜色通道)`。但有时数据会被拉直成一维数组传来（比如从硬件读取）。你想把它变回图片的样子以便处理。

**任务要求：**
你有一个长度为 27 的一维数组 `flat_img`，它其实是一张 **3×3 像素的彩色图**（3 行，3 列，3 个颜色通道 R,G,B）。请将它重塑为正确的三维形状 `(3, 3, 3)`。然后，提取出**红色通道**（即最后一个维度的索引 0），得到二维数组 `red_channel`。

```python
flat_img = np.array([255,0,0, 0,255,0, 0,0,255,   # 第0行像素
                     0,255,0, 255,0,0, 0,0,0,     # 第1行
                     0,0,255, 0,0,0, 255,255,0])  # 第2行

# ========== 你的代码在这里 ==========
img_3d = None          # 重塑成 (3,3,3)
red_channel = None     # 取所有行、所有列，第0个通道
# ===================================

print("三维图像形状:", img_3d.shape)
print("红色通道:\n", red_channel)
```

<details>
<summary><b>✅ 点击查看答案与解析</b></summary>

```python
# 答案代码
img_3d = flat_img.reshape((3, 3, 3))    # 变成3行3列3通道
red_channel = img_3d[:, :, 0]           # 高度取全部，宽度取全部，通道取0

print("三维图像形状:", img_3d.shape)    # (3, 3, 3)
print("红色通道:\n", red_channel)
```

**解析（初中生版）：**
- **reshape** 就像把一列长队的学生按顺序排成 3 层楼，每层 3 排 3 列。总人数 27 不变。
- 重塑时，NumPy 按**行优先**的顺序填数字：先把第一层的第一行填满，接着第一层的第二行…… 就像读书从左到右、从上到下、再从第一页翻到第二页。
- `img_3d[:, :, 0]`：三维索引 `[层, 行, 通道]`。这里我们不管层（高楼），不管行，只取第 0 个通道（红色）。结果是一张 3x3 的红色值。
</details>

---

### 练习题 5：分类标签统计 (np.unique)

**场景故事：**
你有一个图片分类任务，标签 `y` 里存了 100 张图的类别编号（0=猫，1=狗，2=鸟）。在做模型训练前，你需要知道**一共有几个类别**，以及**每个类别的样本数量**，防止数据不平衡（比如鸟只有 5 张，模型会学歪）。

**任务要求：**
用 `np.unique` 函数一次性找出 `y` 中的唯一类别和每个类别出现的次数。

```python
y = np.array([0, 1, 2, 1, 0, 0, 2, 2, 2, 1, 0, 2, 1])

# ========== 你的代码在这里 ==========
unique_labels = None   # 所有出现过的类别
counts = None          # 对应每个类别出现了几次
# ===================================

print("唯一类别:", unique_labels)
print("每个类别的计数:", counts)
# 期望输出类似：唯一类别: [0 1 2]  计数: [4 4 5]
```

<details>
<summary><b>✅ 点击查看答案与解析</b></summary>

```python
# 答案代码
unique_labels, counts = np.unique(y, return_counts=True)

print("唯一类别:", unique_labels)   # [0 1 2]
print("每个类别的计数:", counts)     # 比如 [4 4 5]（取决于数据）
```

**解析（初中生版）：**
- **`np.unique`**：相当于老师说“班里有哪些不同的星座？” 然后开始点名，每个星座报数。
- `return_counts=True` 让函数不仅列出“种类”，还告诉你“每个种类来了几个人”。返回两个数组，一一对应。
- 这在机器学习中非常有用，如果发现某个类别特别少，你可能需要收集更多数据或做特殊处理。
</details>

---

### 🎉 恭喜你！

这 5 道题涵盖了**数据合并、统计描述、异常值清洗、形状变换、类别统计**等数据预处理的核心操作。你已经能用 NumPy 像数据科学家一样思考了！

**课后挑战（选做）：**
1. 尝试将第 4 题的红色通道提取改为**交换通道顺序**（RGB 变 BGR）。
2. 在第 5 题的 `counts` 基础上，计算每个类别的样本占比。

> 继续加油，NumPy 会越来越像你的老朋友！有任何疑问随时问我。