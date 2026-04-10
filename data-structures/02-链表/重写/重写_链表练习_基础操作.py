class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 头部插入
    def insert_at_head(self, data):
        new_node = Node(data) #创建新节点
        new_node.next = self.head #新节点指针（next）指向原来的头结点
        self.head = new_node #头指针指向新节点

        # “=”用来表示“指向”
    
    # 尾部插入
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node #检查头指针的存在
            return
        
        current = self.head #遍历链表的操作，很常用
        while current.next:
            current = current.next
        current.next = new_node

    # 查找
    def search(self, target):
        current = self.head
        while current.next:
            if current == target:
                return True
            current = current.next
        return False    

    
        
        
    