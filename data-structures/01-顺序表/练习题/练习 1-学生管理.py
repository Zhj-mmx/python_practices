# 练习 1：学生成绩管理系统
# 梦哥，独立完成这个练习！
# 要求：用列表操作完成以下功能

# ==================== 数据 ====================
# 学生姓名列表
students = ["张三", "李四", "王五", "赵六", "钱七"]

# 对应的成绩列表（百分制）
scores = [85, 92, 78, 90, 88]


# ==================== 任务 ====================
# 1. 计算平均分
# 2. 找出最高分和最低分的学生
# 3. 筛选出成绩>=90 的优秀学生
# 4. 给每个学生加 5 分（模拟加分政策），但不超过 100
# 5. 按成绩从高到低排序，输出排名

# 你的代码写在这里 ↓
print("=" * 50)
print("学生成绩管理系统")
print("=" * 50)

# TODO: 任务 1 - 计算平均分
def calculate_average(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count
    return average
    


# TODO: 任务 2 - 找出最高分和最低分的学生
def find_highest_and_lowest(students, scores):
    highest_score = max(scores)
    lowest_score = min(scores)
    
    highest_index = scores.index(highest_score)
    lowest_index = scores.index(lowest_score)
    
    highest_student = students[highest_index]
    lowest_student = students[lowest_index]
    
    return highest_student, highest_score, lowest_student, lowest_score


# TODO: 任务 3 - 筛选优秀学生（>=90）
def filter_excellent_students(students, scores):
    excellent_students = []
    for student, score in zip(students, scores):
        if score >= 90:
            excellent_students.append(student)
    return excellent_students


# TODO: 任务 4 - 加分（不超过 100）
def add_bonus_points(students, scores, bonus):
    for i in range(len(scores)):
        scores[i] += bonus
        if scores[i] > 100:
            scores[i] = 100
    return students, scores


# TODO: 任务 5 - 排序并输出排名
def sort_and_display_ranking(students, scores):
    # 将学生和成绩配对，然后按成绩降序排列
    student_scores = list(zip(students, scores))
    student_scores.sort(key=lambda x: x[1], reverse=True)

    print("学生排名:")
    for i, (student, score) in enumerate(student_scores, start=1):
        print(f"{i}. {student}: {score}")


print("=" * 50)
print("✅ 练习完成！")
