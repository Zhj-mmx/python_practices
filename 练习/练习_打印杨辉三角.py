def f(n):
    for x in range(n):
        list = [1,1]
        new_list = []
        if x == 1:
            print(1)
        elif x == 2:
            print(1,1)
        elif x > 2:
            for i in range(1,x):
                new_list.insert(i,list(i-1) + list(i))
                list = new_list
                for each in list:
                    print(list(each),end = " ")
            
#以下为参考答案
def fun(n):
    a = []
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(0)
    for i in range(n):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2,n):
        for j in range(1,i):
            a[i][j]=a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(str(a[i][j]),end="")
        print()
                  
def main():
    fun(5)

if __name__=='__main__':
    main()

        

        

        
                    



            
