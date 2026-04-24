import numpy as np

X = np.array([
    [120, 3,5],
    [85, 2, 20],
    [200, 4, 2],
    [60, 1, 40]
    ])
y = np.array([350, 180, 620, 90])

print("特征矩阵 X:\n", X)
print("标签向量 y:", y)
print("X 的形状应为 (4, 3)，实际为:", X.shape)
