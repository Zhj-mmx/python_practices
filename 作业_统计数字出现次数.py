def count_digits():
    s = input("请输入一串数字")
    count = {}
    for n in s:
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1
    for i in range(10):
        digit = str(i)
        print(f"数字{i}的数量是{count.get(digit,0)}")
        
count_digits()                                        
