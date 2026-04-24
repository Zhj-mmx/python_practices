class 机器人:
    def __init__(self,名字,电量=100):
        self.名字 = 名字
        self.电量 = 电量
        self.技能列表 = ["移动","充电"]

    def __str__(self):
        return f"机器人[{self.名字}]电量：{self.电量}%"

    def __repr__(self):
        return f"机器人('{self.名字}', 电量={self.电量})"

    def __len__(self):
        """定义len(对象)的行为"""
        return len(self.技能列表)
    
    def __add__(self, 其他机器人):
        """定义 + 运算符行为 - 机器人合体！"""
        新名字 = f"{self.名字}+{其他机器人.名字}"
        新电量 = self.电量 + 其他机器人.电量
        return 机器人(新名字, 新电量)

机器人1 = 机器人("小机", 80)
机器人2 = 机器人("小器", 70)

print(str(机器人1))      # 输出: 机器人[小机] 电量:80%
print(repr(机器人1))     # 输出: 机器人('小机', 电量=80)
print(len(机器人1))      # 输出: 2

合体机器人 = 机器人1 + 机器人2
print(合体机器人)       
