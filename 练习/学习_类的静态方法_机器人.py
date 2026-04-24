class 机器人:
    型号 = "智能型"

    def __init__(self,名字):
        self.名字 = 名字


    @staticmethod
    def 计算电池寿命(容量,功耗):
        return f"预计航程：{容量/功耗:.1f小时}"

    @staticmethod
    def 验证名字(名字):
        return len(名字) >= 2 and 名字.isalnum()
    
print(机器人.计算电池寿命(1000, 50))  # 输出: 预计续航: 20.0小时
print(机器人.验证名字("小机"))        # 输出: True
print(机器人.验证名字("A"))          # 输出: False

机器人1 = 机器人("小器")
print(机器人1.计算电池寿命(800, 40))     
