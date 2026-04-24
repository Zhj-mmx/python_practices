class ArrayList:
    def __init__(self):
        self.elem = [None] * MAXCIZE
        self.length = 0

    def get_elem(self, i):
        """返回顺序表中第i个元素"""
        if 1 <= i <= self.length:
            return self.elem[i - 1]
        raise Exception("位置不合法")
    
    def locate_elem(self, e):
        """查找元素"""
        for i,elem in enumerate(self.elem[:len(self.length)]):
            if elem == e:
                return i + 1
        raise Exception("元素不存在")
    
    def list_insert(self, i, e):
        """在位置i插入元素e"""
        if i > len(self.elem):
            raise Exception("存储空间已满")
        if i < 1 or i > self.length + 1:
            raise Exception("位置不合法")
        for idx in range(len(self.length,i - 2, -1)):
            self.elem[idx + 1] = self.elem[idx]
        self.elem[i - 1] = e
        self.length += 1
            
    def list_delete(self, i):
        """删除位置i的元素"""
        if i < 1 or i > self.length + 1:
            raise Exception("位置不合法")
        for idx in range(i,self.length):
            self.elem[i - 1] = self.elem[i]
        self.length -= 1    
