import numpy as np

np.random.seed(42)

data = np.random.randint(1, 100, size=(3, 3))
print("原始数据:\n", data)

mean_col = data.mean(axis=0)
std_col = data.std(axis=0)

normalized = (data - mean_col) /std_col

print("\n标准化后数据:\n", normalized.round(4))

print("\n新均值 (接近0):", normalized.mean(axis=0).round(6))
print("新标准差 (接近1):", normalized.std(axis=0).round(6))