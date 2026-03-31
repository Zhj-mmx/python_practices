class 学生:
    def __init__(self, 姓名, 学号):
        self.姓名 = 姓名
        self.学号 = 学号
        self.成绩 = {}
    
    def 添加成绩(self, 科目, 分数):
        self.成绩[科目] = 分数
        print(f"{self.姓名}的{科目}成绩: {分数}")
    
    def 查看成绩单(self):
        print(f"{self.姓名}的成绩单:")
        for 科目, 分数 in self.成绩.items():
            print(f"  {科目}: {分数}")
    
    def 计算平均分(self):
        if not self.成绩:
            return 0
        总分 = sum(self.成绩.values())
        return 总分 / len(self.成绩)

# 测试你的代码
学生1 = 学生("小明", "2024001")
学生1.添加成绩("数学", 90)
学生1.添加成绩("英语", 85)
学生1.查看成绩单()
print(f"平均分: {学生1.计算平均分()}")
