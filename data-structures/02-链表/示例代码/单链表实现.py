# 单链表完整实现
# 梦哥，先理解这个，再去做练习！

class Node:
    """链表节点"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """单链表"""
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """判断是否为空"""
        return self.head is None
    
    def insert_at_head(self, data):
        """头部插入"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"✓ 头部插入：{data}")
    
    def insert_at_tail(self, data):
        """尾部插入"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"✓ 尾部插入：{data}")
    
    def insert_at(self, position, data):
        """指定位置插入"""
        if position == 0:
            self.insert_at_head(data)
            return
        
        new_node = Node(data)
        current = self.head
        count = 0
        
        # 找到插入位置的前一个节点
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current is None:
            print(f"✗ 位置 {position} 超出范围")
            return
        
        new_node.next = current.next
        current.next = new_node
        print(f"✓ 位置 {position} 插入：{data}")
    
    def delete(self, data):
        """删除指定值的节点"""
        if self.is_empty():
            print(f"✗ 链表为空，无法删除 {data}")
            return
        
        # 删除头节点
        if self.head.data == data:
            self.head = self.head.next
            print(f"✓ 删除：{data}")
            return
        
        # 遍历查找
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                print(f"✓ 删除：{data}")
                return
            current = current.next
        
        print(f"✗ 未找到：{data}")
    
    def search(self, data):
        """查找元素"""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def display(self):
        """打印链表"""
        if self.is_empty():
            print("链表为空")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" → ".join(elements) + " → None")
    
    def get_length(self):
        """获取长度"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def reverse(self):
        """反转链表（重要！）"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  # 保存下一个节点
            current.next = prev       # 反转指针
            prev = current            # 移动 prev
            current = next_node       # 移动 current
        
        self.head = prev  # 更新头节点
        print("✓ 链表已反转")


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("单链表操作演示")
    print("=" * 50)
    
    # 创建链表
    ll = LinkedList()
    
    # 尾部插入
    print("\n【尾部插入】")
    ll.insert_at_tail(10)
    ll.insert_at_tail(20)
    ll.insert_at_tail(30)
    ll.display()
    
    # 头部插入
    print("\n【头部插入】")
    ll.insert_at_head(5)
    ll.display()
    
    # 指定位置插入
    print("\n【指定位置插入】")
    ll.insert_at(2, 15)
    ll.display()
    
    # 查找
    print("\n【查找】")
    pos = ll.search(20)
    print(f"20 的位置：{pos}")
    pos = ll.search(100)
    print(f"100 的位置：{pos}")
    
    # 删除
    print("\n【删除】")
    ll.delete(15)
    ll.display()
    
    # 长度
    print("\n【长度】")
    print(f"链表长度：{ll.get_length()}")
    
    # 反转
    print("\n【反转】")
    ll.reverse()
    ll.display()
    
    print("\n" + "=" * 50)
    print("✅ 演示完成！")
