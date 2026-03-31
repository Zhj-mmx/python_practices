# 练习 2：反转链表 II - 反转指定区间
# 梦哥，这是 LeetCode 92 题，考察对指针操作的精细控制！

# ==================== 任务 ====================
# 1. 理解题目要求：只反转链表中 [left, right] 区间的节点
# 2. 完成下面的函数
# 3. 测试你的代码（注意边界情况！）

# ==================== 节点定义 ====================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ==================== 题目 ====================
def reverse_between(head, left, right):
    """
    反转链表中从位置 left 到位置 right 的节点
    
    输入示例：
        链表：1 → 2 → 3 → 4 → 5 → None
        left = 2, right = 4
        输出：1 → 4 → 3 → 2 → 5 → None
    
    思路提示：
    1. 用 dummy 节点处理边界（left=1 时头节点会变）
    2. 找到第 left-1 个节点（记为 prev）
    3. 第 left 个节点（记为 start）反转后会变成尾
    4. 对 [left, right] 区间执行反转（反转 right-left 次）
    5. 重新连接：prev → 新头，旧尾 → right+1 位置的节点
    
    关键：画图！标出每个指针的位置！
    """
    # TODO: 梦哥，你来写！
    # 提示：需要记录 prev, start, curr 三个关键位置
    pass


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
    print("=" * 60)
    print("反转链表 II - 测试用例")
    print("=" * 60)
    
    # 测试 1：一般情况
    print("\n【测试 1】一般情况")
    head = create_list([1, 2, 3, 4, 5])
    print(f"原始：", end="")
    print_list(head)
    print(f"反转区间 [2, 4]")
    result = reverse_between(head, 2, 4)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：1 → 4 → 3 → 2 → 5 → None")
    
    # 测试 2：从头开始反转
    print("\n【测试 2】从头开始反转（left=1）")
    head = create_list([1, 2, 3, 4, 5])
    print(f"原始：", end="")
    print_list(head)
    print(f"反转区间 [1, 3]")
    result = reverse_between(head, 1, 3)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：3 → 2 → 1 → 4 → 5 → None")
    
    # 测试 3：整个链表反转
    print("\n【测试 3】整个链表反转")
    head = create_list([1, 2, 3, 4, 5])
    print(f"原始：", end="")
    print_list(head)
    print(f"反转区间 [1, 5]")
    result = reverse_between(head, 1, 5)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：5 → 4 → 3 → 2 → 1 → None")
    
    # 测试 4：只反转一个节点（left=right）
    print("\n【测试 4】只反转一个节点（left=right）")
    head = create_list([1, 2, 3, 4, 5])
    print(f"原始：", end="")
    print_list(head)
    print(f"反转区间 [3, 3]")
    result = reverse_between(head, 3, 3)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：1 → 2 → 3 → 4 → 5 → None（不变）")
    
    # 测试 5：只有两个节点
    print("\n【测试 5】只有两个节点")
    head = create_list([3, 5])
    print(f"原始：", end="")
    print_list(head)
    print(f"反转区间 [1, 2]")
    result = reverse_between(head, 1, 2)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：5 → 3 → None")
    
    print("\n" + "=" * 60)
    print("练习完成！检查所有测试用例是否通过！")
    print("=" * 60)
