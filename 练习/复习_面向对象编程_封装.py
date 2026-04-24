class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 私有属性，外部不能直接访问
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

    def print_balance(self):
        print(self.__balance)

# 使用：只能通过规定的方法操作
account = BankAccount(1000)
account.deposit(500)  # ✅ 正确方式
# account.__balance = 2000  # ❌ 错误！不能直接修改
print(account.get_balance())
account.withdraw(500)
print(account.get_balance())
my_account = BankAccount(2000)
my_account.deposit(2399)
my_account.print_balance()




