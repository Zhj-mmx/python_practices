class SupermarketCheckout:
    def __init__(self):
        self.products = {
            '36012348': {'name': '矿泉水', 'price': 3.00},
            '36012341': {'name': '可乐', 'price': 3.50},
            '36012342': {'name': '薯片', 'price': 5.80},
            '36012343': {'name': '面包', 'price': 7.60},
            '36012344': {'name': '牛奶', 'price': 6.40},
            '36012345': {'name': '鸡蛋', 'price': 1.50}
        }
        self.cart = []  
        self.total_amount = 0.0  

    def scan_products(self):
        print("欢迎使用超市自助结账系统")
        print("提示：请扫描商品条形码(8位），输入0结束扫描")
        print("#" * 40)
        
        while True:
            try:
                barcode = input("请扫描商品条形码（输入0结束）：").strip()
                
                if barcode == '0':
                    break
                
                if len(barcode) != 8:
                    print(f"错误：未找到条形码为 {barcode} 的商品，请重新扫描")
                    continue
                
                if barcode not in self.products:
                    print(f"错误：未找到条形码为 {barcode} 的商品，请重新扫描")
                    continue
                
                product = self.products[barcode]
                print(f"已添加：{product['name']}，单价：￥{product['price']:.2f}")
                
                while True:
                    try:
                        quantity_input = input(f"请输入{product['name']}的数量：")
                        quantity = int(quantity_input)
                        
                        if quantity <= 0:
                            print("数量必须为正整数，请重新输入")
                            continue
                            
                        break
                    except ValueError:
                        print("请输入有效的整数数量")
                
                subtotal = product['price'] * quantity
                
                self.cart.append({
                    'name': product['name'],
                    'price': product['price'],
                    'quantity': quantity,
                    'subtotal': subtotal
                })
                
                self.total_amount += subtotal
                
            except KeyboardInterrupt:
                print("\n程序已退出")
                return False
            except Exception as e:
                print(f"发生错误：{e}")
        
        return True

    def display_receipt(self):
        if not self.cart:
            print("购物车为空！")
            return
        
        print("\n您的购物清单：")
        print("商品名称".ljust(10) + "单价（元）".ljust(12) + "数量".ljust(8) + "小计（元）")
        print("-" * 45)
        
        for item in self.cart:
            name = item['name'].ljust(8)
            price = f"{item['price']:.2f}".ljust(10)
            quantity = str(item['quantity']).ljust(6)
            subtotal = f"{item['subtotal']:.2f}"
            print(f"{name}{price}{quantity}{subtotal}")
        
        print("-" * 45)
        print(f"总计：￥{self.total_amount:.2f}")

    def process_payment(self):
        if self.total_amount == 0:
            print("无需支付！")
            return True
        
        print("\n请选择支付方式：")
        print("1. 现金支付")
        print("2. 支付宝")
        print("3. 微信支付")
        
        while True:
            try:
                choice = input("请输入支付方式编号：").strip()
                
                if choice == '1':
                    return self.cash_payment()
                elif choice == '2':
                    return self.alipay_payment()
                elif choice == '3':
                    return self.wechat_payment()
                else:
                    print("无效的支付方式，请重新输入")
                    
            except KeyboardInterrupt:
                print("\n支付已取消")
                return False
            except Exception as e:
                print(f"支付错误：{e}")

    def cash_payment(self):
        print("\n正在使用现金支付...")
        print(f"应付金额：￥{self.total_amount:.2f}")
        
        while True:
            try:
                cash = float(input("请输入支付金额："))
                
                if cash < self.total_amount:
                    shortage = self.total_amount - cash
                    print(f"金额不足，还差￥{shortage:.2f}，请重新输入")
                    continue
                
                change = cash - self.total_amount
                if change > 0:
                    print(f"找零：￥{change:.2f}")
                
                print("支付成功！")
                return True
                
            except ValueError:
                print("请输入有效的金额")
            except Exception as e:
                print(f"支付错误：{e}")

    def alipay_payment(self):

        print(f"\n正在使用支付宝支付￥{self.total_amount:.2f}...")
        
        import time
        print("请打开支付宝扫描二维码...")
        time.sleep(1)
        print("正在验证支付...")
        time.sleep(1)
        print("✅ 支付宝支付成功！")
        return True

    def wechat_payment(self):
 
        print(f"\n正在使用微信支付￥{self.total_amount:.2f}...")
        
        import time
        print("请打开微信扫描二维码...")
        time.sleep(1)
        print("正在验证支付...")
        time.sleep(1)
        print("✅ 微信支付成功！")
        return True

    def run(self):

        if not self.scan_products():
            return
        
        if not self.cart:
            print("您没有购买任何商品！")
            return
        
        self.display_receipt()
        
        if self.process_payment():
            print("\n感谢您的光临，欢迎下次再来！")
        else:
            print("\n支付失败，请重新尝试。")

if __name__ == "__main__":
 
    checkout_system = SupermarketCheckout()
    checkout_system.run()
