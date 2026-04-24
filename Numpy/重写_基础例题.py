import numpy as np

X = np.array([
    [120,   3,  5],
    [ 85,   2, 20],
    [200,   4,  2],
    [ 60,   1, 40]
])

y = np.array([350, 180, 620, 90])

area = X[:,0]
subset = X[:2, :2]

is_old = X[:,2] > 10
old_house_X = X[is_old]
#old_house_X = X[X[:, 2] > 10]

expensive_y = y[y > 200]

print("老房子特征:\n", old_house_X)
print("豪宅价格:", expensive_y)

area_col = X[:,1]
area_min = area_col.min()
area_max = area_col.max()

area_norm = (area_col - area_min)/(area_max - area_min)
area_norm = np.round(area_norm, 2)

print("原始面积:", area_col)
print("归一化后:", area_norm)

y_true = np.array([350, 180, 620, 90])
y_pred = np.array([320, 200, 600, 120])

mae = np.mean(np.abs(y_true - y_pred))

print("平均绝对误差 MAE:", mae)

w = [2.5, 10, -1] 
b = 30

y_pred_new = X @ w + b
# 或者使用 np.dot(X, w) + b

print("预测房价:", y_pred_new)

np.random.seed(42)  # 固定随机结果，方便对答案
X = np.array([[120, 3, 5],
              [85, 2, 20],
              [200, 4, 2],
              [60, 1, 40]])
y = np.array([350, 180, 620, 90])

n_samples = X.shape[0] 
shuffle_idx = np.random.permutation(n_samples)
X_shuffled = X[shuffle_idx]
y_shuffled = y[shuffle_idx]

print("打乱后的索引顺序:", shuffle_idx)
print("打乱后 X:\n", X_shuffled)
print("打乱后 y:", y_shuffled)