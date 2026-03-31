# 练习 2：实验数据过滤
# 梦哥，这个练习模拟你们课题组的真实场景！

# ==================== 数据 ====================
# 小鼠实验数据：[小鼠 ID, 组别, 体重变化%, 焦虑改善%, 蛋白表达量]
raw_data = [
    ["M001", "control", 2.5, 15, 0.45],
    ["M002", "control", -1.2, 10, 0.42],
    ["M003", "treatment_A", 8.5, 35, 0.38],
    ["M004", "treatment_A", 6.2, 28, 0.40],
    ["M005", "treatment_B", 3.1, 42, 0.35],
    ["M006", "treatment_B", -2.5, 38, 0.33],
    ["M007", "treatment_C", 9.8, 32, 0.48],
    ["M008", "treatment_C", 7.5, 45, 0.50],
    ["M009", "treatment_D", -5.2, 20, 0.30],
    ["M010", "treatment_D", 1.8, 25, 0.32],
]

# 判定标准
ANXIETY_THRESHOLD = 30      # 焦虑改善≥30%
SENSITIZATION_THRESHOLD = 40  # 行为敏化改善≥40%


# ==================== 任务 ====================
# 1. 筛选出"适合疗法"的小鼠（焦虑改善≥30% 且 体重变化>0）
# 2. 按组别分组统计每组的小鼠数量
# 3. 计算每组的平均焦虑改善率
# 4. 找出蛋白表达量最高和最低的小鼠
# 5. 生成报告：输出适合疗法的小鼠列表

# 你的代码写在这里 ↓
print("=" * 60)
print("实验数据过滤分析")
print("=" * 60)

# TODO: 任务 1 - 筛选适合疗法的小鼠
def filter_suitable_mice(data):
    suitable_mice = []
    for record in data:
        mouse_id, group, weight_change, anxiety_improvement, protein_expression = record
        if anxiety_improvement >= ANXIETY_THRESHOLD and weight_change > 0 :
            suitable_mice.append(record)
    return suitable_mice



# TODO: 任务 2 - 按组别统计数量
def count_by_group(data):
    group_counts = {}
    for record in data:
        group = record[1]
        if group not in group_counts:
            group_counts[group] = 0
        group_counts[group] += 1
    return group_counts


# TODO: 任务 3 - 计算每组平均焦虑改善率
def average_anxiety_improvement_by_group(data):
    """不是很懂这个题的思路，先写个简单版本，后续再优化"""
    group_improvements = {}
    group_counts = {}
    for record in data:
        group = record[1]
        if group not in group_improvements:
            group_improvements[group] = 0
        group_improvements[group] += record[3]
        group_counts[group] += 1

    # 计算平均值
    for group in group_improvements:
        group_improvements[group] /= group_counts[group]

    return group_improvements





# TODO: 任务 4 - 找出蛋白表达量极值
def find_protein_expression_extremes(data):
    highest_expression = float('-inf')
    lowest_expression = float('inf') 
    highest_mouse = None
    lowest_mouse = None

    for record in data:
        mouse_id, group, weight_change, anxiety_improvement, protein_expression = record
        if protein_expression > highest_expression:
            highest_expression = protein_expression
            highest_mouse = record
        if protein_expression < lowest_expression:
            lowest_expression = protein_expression
            lowest_mouse = record

    return highest_mouse, lowest_mouse


# TODO: 任务 5 - 生成报告
def generate_report(suitable_mice):
    print("适合疗法的小鼠列表：")
    for mouse in suitable_mice:
        print(f"ID: {mouse[0]}, 组别: {mouse[1]}, 体重变化: {mouse[2]}%, 焦虑改善: {mouse[3]}%, 蛋白表达量: {mouse[4]}")


print("=" * 60)
print("✅ 练习完成！")
