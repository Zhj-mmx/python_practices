# 练习 1：链表反转
# 梦哥，这是一个经典的链表面试题！

# ==================== 任务 ====================
# 1. 先运行并理解 `示例代码/单链表实现.py`
# 2. 完成下面的链表反转函数（有两种方法）
# 3. 测试你的代码

# ==================== 节点定义 ====================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ==================== 方法 1：迭代法 ====================
def reverse_iterative(head):
    """
    迭代法反转链表
    
    思路：
    1. 用三个指针：prev, current, next_node
    2. 逐个反转每个节点的指针方向
    3. 最后返回新的头节点
    """
    prev = None
    current = head
    while current:
        next_node = current.next  # 1. 保存下一个节点
        current.next = prev       # 2. 反转指针
        prev = current            # 3. prev 前移
        current = next_node       # 4. current 前移
    return prev  # 新的头节点

    """
    for prev in data:
        current = prev.next
        next_code = prev.next.next
        current.next = prev
        prev = current
    self.head = None
    self.head.next = prev
    """    

# ==================== 方法 2：递归法（挑战！） ====================
def reverse_recursive(head):
    """
    递归法反转链表
    
    思路：
    1. 递归到链表末尾（基础情况）
    2. 回溯时反转指针：让后面节点的 next 指向自己
    3. 自己的 next 置为 None，避免成环
    4. 返回新的头节点（最开始的最后一个节点）
    """
    # 基础情况：空链表或只有一个节点
    if not head or not head.next:
        return head
    
    # 递归反转后面的部分
    new_head = reverse_recursive(head.next)
    
    # 反转当前节点和下一个节点的连接
    head.next.next = head  # 让后面的节点指向自己
    head.next = None       # 自己的 next 置空，避免成环
    
    return new_head  # 一直返回最开始的 new_head


# ==================== 辅助函数 ====================
def create_list(values):
    """从列表创建链表"""
    if not values:
        return None
    
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def print_list(head):
    """打印链表"""
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" → ".join(elements) + " → None")


# ==================== 测试 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("链表反转练习 - 两种方法对比")
    print("=" * 50)
    
    # 测试数据
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [100],
        []
    ]
    
    for i, values in enumerate(test_cases, 1):
        print(f"\n【测试 {i}】")
        print(f"原始链表：", end="")
        head = create_list(values)
        print_list(head)
        
        # 迭代法
        print(f"迭代法：  ", end="")
        head1 = create_list(values)  # 重新创建，因为反转后原链表变了
        new_head1 = reverse_iterative(head1)
        print_list(new_head1)
        
        # 递归法
        print(f"递归法：  ", end="")
        head2 = create_list(values)  # 重新创建
        new_head2 = reverse_recursive(head2)
        print_list(new_head2)
    
    print("\n" + "=" * 50)
    print("练习完成！")
    print("提示：两种方法结果应该一样！")
    print("=" * 50)
