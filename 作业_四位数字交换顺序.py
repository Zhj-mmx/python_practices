num = input("请输入一个四位整数：")

if len(num) == 4 and num.isdigit():
    new_num = num[2] + num[3] + num[0] + num[1]
    
    print(f"输入：{num}")
    print(f"输出：{new_num}")
else:
    print("输入错误，请确保输入的是四位整数！")
