import numpy as np

adj_matrix = np.zeros((4,4), dtype=int)
adj_matrix[0,1] = adj_matrix[1,0] = 1
adj_matrix[0,2] = adj_matrix[2,0] = 1
adj_matrix[1,3] = adj_matrix[3,1] = 1
adj_matrix[2,3] = adj_matrix[3,2] = 1


print("校园邻接矩阵：")
print(adj_matrix)
print("A 和 C 是否直接相连？", adj_matrix[0, 2] == 1)

