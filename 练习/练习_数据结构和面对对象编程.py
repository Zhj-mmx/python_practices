echo '# 4. 实际应用：电商商品系统
class 商品:
    def __init__(self, 名字, 价格, 库存):
        self.名字 = 名字
        self.价格 = 价格
        self.库存 = 库存
        self.是否上架 = True
    
    def 显示信息(self):
        状态 = "在售" if self.是否上架 else "下架"
        return f"{self.名字} - {self.价格}元 (库存: {self.库存}, 状态: {状态})"
    
    def 购买(self, 数量=1):
        if self.库存 >= 数量:
            self.库存 -= 数量
            return f"成功购买{数量}个{self.名字}，花费{self.价格 * 数量}元"
        else:
            return f"库存不足！只剩{self.库存}个{self.名字}"

class 电子产品(商品):
    def __init__(self, 名字, 价格, 库存, 品牌, 保修期):
        super().__init__(名字, 价格, 库存)
        self.品牌 = 品牌
        self.保修期 = 保修期  # 月为单位
    
    def 显示信息(self):
        base_info = super().显示信息()
        return f"{base_info} - 品牌: {self.品牌}, 保修: {self.保修期}个月"
    
    def 维修服务(self):
        return f"{self.品牌}{self.名字}享受{self.保修期}个月保修服务"

class 食品(商品):
    def __init__(self, 名字, 价格, 库存, 保质期):
        super().__init__(名字, 价格, 库存)
        self.保质期 = 保质期  # 天数
    
    def 显示信息(self):
        base_info = super().显示信息()
        return f"{base_info} - 保质期: {self.保质期}天"
    
    def 检查新鲜度(self):
        if self.保质期 > 7:
            return "🔥 很新鲜！"
        elif self.保质期 > 3:
            return "✅ 还可以"
        else:
            return "⚠️ 尽快食用！"

print("=== 电商商品系统 ===")
# 创建各种商品
手机 = 电子产品("智能手机", 2999, 50, "华为", 24)
电脑 = 电子产品("游戏笔记本", 8999, 10, "联想", 36)
巧克力 = 食品("巧克力", 25, 100, 30)
牛奶 = 食品("鲜牛奶", 8, 20, 5)

print("商品列表:")
print("1.", 手机.显示信息())
print("2.", 电脑.显示信息()) 
print("3.", 巧克力.显示信息())
print("4.", 牛奶.显示信息())

print("\n=== 特殊功能 ===")
print(手机.维修服务())
print(电脑.维修服务())
print(巧克力.检查新鲜度())
print(牛奶.检查新鲜度())

print("\n=== 购买测试 ===")
print(手机.购买(2))
print(巧克力.购买(5))
print(牛奶.购买(25))  # 测试库存不足' > class_ecommerce.py

python class_ecommerce.py
