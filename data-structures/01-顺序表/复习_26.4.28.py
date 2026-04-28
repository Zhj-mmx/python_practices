#复习一下顺序表

# 列表推导式
matrix = [[i*j for i in range(3)] for j in range(3) if j > 0]
print(matrix)

#解包
a, b, c = [1, 2, 3]

first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)

lst = [x for x in lst if x % 2 != 0]