adj_list = {'A':['B','C'],
            'B':['A','D'],
            'C':['A','D'],
            'D':['B','C']  
}

print("校园邻接表：")
for node, neighbors in adj_list.items():
    print(f"{node}的门卫说:我可以直接去 {neighbors}")
    