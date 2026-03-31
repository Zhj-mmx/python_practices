list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
1.
list3 = list1 + list2
2.
list4 = []
for i in list3:
    if i not in list1 or i not in list2:
        list4.append(i)
3.
list5 = []
for each in list1:
    if each in list2:
        list5.append(each)
4.
list6 = [] 
for each in list1:
    if each not in list2:
        list6.append(each)
        
print(list3)       
print(list4)    
print(list5)
print(list6)
