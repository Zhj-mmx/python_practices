def index_kmp(s, t, pos, next):
    i = pos
    j = 1
    while i <= s.length and j <= t.length:
        if j == 0 or s.ch[i]==t.ch[j]:
            i += 1
            j += 1 #指针相同，并一起向右滑动
        else:
            j = next[j] #滑动j指针到合适的k位置，不用像之前一样回到1位置
        if j > t.length:
            return i - t.length #匹配成功，返回i的位置
        else:
            return 0 #匹配失败    
        
#下面设计next函数
def get_next(t):
    next = [0] * (t.length + 1)
    i = 1
    j = 0
    while i < t.length:
        if j == 0 or t.ch[i] == t.ch[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next
