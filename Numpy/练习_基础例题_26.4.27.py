import numpy as np

train = np.array([[78, 85, 90],
                  [65, 72, 88]])    # 学生A、B

test  = np.array([[92, 88, 95],
                  [55, 60, 70]])    # 学生C、D

bonus = np.array([[5],
                  [5],
                  [10],
                  [0]])             # 每个学生的额外加分

all_data = np.vstack((train, test))

full_data = np.hstack((all_data, bonus))

print("合并后的全量数据 (4x3):\n", all_data)
print("加上加分列后 (4x4):\n", full_data)
print("full_data 形状:", full_data.shape)


scores = np.array([[78, 85, 90],
                   [65, 72, 88],
                   [92, 88, 95],
                   [55, 60, 70]])

mean_score = np.mean(scores, axis=0)
std_score = np.std(scores, axis=0)
median_score = np.median(scores, axis=0)
max_score = np.max(scores, axis=0)
min_score = np.min(scores, axis=0)

max_score_row = np.resize(np.max(scores, axis=1), (4, 1))

print("平均分:", mean_score)
print("标准差:", std_score)
print("中位数:", median_score)
print("最高分:", max_score)
print("最低分:", min_score)

print("每个学生的最高分:", max_score_row)



temps = np.array([[ 25, -999,   30],
                  [ 27,   22,   33],
                  [-999,  21,   35],
                  [ 28,   20,  -999],
                  [ 26,   23,   31]])

fault_mask = (temps == -999)

normal_sum = np.where(fault_mask, 0, temps).sum(axis=0)

normal_count = (~fault_mask).sum(axis=0)

mean_normal = normal_sum / normal_count

temps_cleaned = np.where(fault_mask, mean_normal, temps)

print("故障掩码:\n", fault_mask)
print("每列正常均值:", mean_normal)
print("清洗后的温度:\n", temps_cleaned)