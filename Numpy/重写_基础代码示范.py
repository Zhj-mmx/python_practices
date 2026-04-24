import numpy as np

# ---------- 1. 创建数组 ----------
a = np.array([1,2,3])
b = np.array([[1,2],[3,4]])
c = np.zeros((2,3))
d = np.ones((2,3), dtype=np.int32)
e = np.arange(10, 20, 2)
f = np.linspace(0, 1 ,5)

print("a =", a)
print("b =\n", b)
print("e =", e)

#[Running] python -u "d:\Python_code\Numpy\重写_基础代码示范.py"
#a = [1 2 3]
#b =
# [[1 2]
#[3 4]]
# e = [10 12 14 16 18]


# ---------- 2. 属性 ----------
print("b的形状:", b.shape)     # (2, 2)
print("b的维度:", b.ndim)      # 2
print("b的元素总数:", b.size)  # 4
print("b的数据类型:", b.dtype) # int64 (根据系统)
