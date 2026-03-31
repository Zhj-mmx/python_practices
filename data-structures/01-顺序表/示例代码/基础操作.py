# 顺序表基础操作示例
# 梦哥，运行这个文件熟悉基本操作

# ==================== 1. 创建列表 ====================
print("=== 创建列表 ===")

# 空列表
empty = []
print(f"空列表：{empty}")

# 小鼠实验数据（体重）
weights = [25.3, 26.1, 24.8, 25.5, 25.0, 24.6, 25.2, 25.8, 24.9, 25.1]
print(f"小鼠体重数据：{weights}")

# 列表推导式 - 生成 1-10 的平方
squares = [x**2 for x in range(1, 11)]
print(f"1-10 的平方：{squares}")


# ==================== 2. 访问元素 ====================
print("\n=== 访问元素 ===")

print(f"第 1 只小鼠体重：{weights[0]}")
print(f"最后 1 只小鼠体重：{weights[-1]}")
print(f"前 3 只小鼠：{weights[:3]}")
print(f"后 3 只小鼠：{weights[-3:]}")
print(f"隔一只取一只：{weights[::2]}")


# ==================== 3. 增删改 ====================
print("\n=== 增删改 ===")

# 追加新数据
weights.append(26.5)
print(f"追加后：{weights}")

# 插入到指定位置
weights.insert(0, 25.0)  # 在开头插入
print(f"开头插入后：{weights}")

# 修改元素
weights[0] = 24.5
print(f"修改后：{weights}")

# 删除末尾
last = weights.pop()
print(f"删除末尾 {last}，剩余：{weights}")


# ==================== 4. 统计计算 ====================
print("\n=== 统计计算 ===")

print(f"小鼠数量：{len(weights)}")
print(f"平均体重：{sum(weights)/len(weights):.2f}")
print(f"最重：{max(weights)}")
print(f"最轻：{min(weights)}")

# 排序
sorted_weights = sorted(weights)
print(f"排序后：{sorted_weights}")


# ==================== 5. 列表推导式实战 ====================
print("\n=== 列表推导式实战 ===")

# 筛选体重 > 25 的小鼠
heavy_mice = [w for w in weights if w > 25]
print(f"体重>25 的小鼠：{heavy_mice}")

# 计算每只小鼠体重的平方（模拟某种转换）
weight_squared = [w**2 for w in weights]
print(f"体重平方：{[f'{w:.1f}' for w in weight_squared]}")

# 带条件的转换：体重>25 的标记为"H"，否则"L"
labels = ["H" if w > 25 else "L" for w in weights]
print(f"高低分组：{labels}")


# ==================== 6. 解包 ====================
print("\n=== 解包 ===")

first, *middle, last = weights
print(f"第一只：{first}")
print(f"中间：{middle}")
print(f"最后一只：{last}")

print("\n✅ 示例运行完成！")
