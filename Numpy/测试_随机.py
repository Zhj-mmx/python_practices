import numpy as np

#np.random.seed(42)
X = np.array([[120, 3, 5],
              [85, 2, 20],
              [200, 4, 2],
              [60, 1, 40]])
y = np.array([350, 180, 620, 90])

# 答案代码
n_samples = X.shape[0]                 # 结果是 4
shuffle_idx = np.random.permutation(n_samples)  # 例如 [2, 0, 3, 1]
X_shuffled = X[shuffle_idx]            # 按照新顺序取行
y_shuffled = y[shuffle_idx]            # 用同样的顺序取标签

print("打乱后的索引顺序:", shuffle_idx)
print("打乱后 X:\n", X_shuffled)
print("打乱后 y:", y_shuffled)