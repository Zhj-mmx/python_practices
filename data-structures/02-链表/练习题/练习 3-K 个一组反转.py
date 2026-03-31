# 练习 3：K 个一组反转链表
# 梦哥，这是 LeetCode 25 题，链表反转的巅峰之作！

# ==================== 任务 ====================
# 1. 理解题目：每 k 个节点一组进行反转，不足 k 个的保持不变
# 2. 完成下面的函数（推荐用递归，更简洁！）
# 3. 测试你的代码

# ==================== 节点定义 ====================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ==================== 题目 ====================
def reverse_k_group(head, k):
    """
    K 个一组反转链表
    
    输入示例 1：
        链表：1 → 2 → 3 → 4 → 5 → None
        k = 2
        输出：2 → 1 → 4 → 3 → 5 → None
    
    输入示例 2：
        链表：1 → 2 → 3 → 4 → 5 → None
        k = 3
        输出：3 → 2 → 1 → 4 → 5 → None
    
    思路提示（递归法）：
    1. 先检查剩余节点是否足够 k 个（不足则直接返回 head）
    2. 如果足够，反转前 k 个节点
    3. 递归处理剩余部分：head.next = reverse_k_group(剩余，k)
    4. 返回新的头节点
    
    关键点：
    - 先检查再反转！不足 k 个时保持不变
    - 递归版比迭代版简洁很多
    - 相信函数定义：reverse_k_group 已经能处理任意链表
    
    挑战：试试用迭代法也实现一遍！
    """
    # TODO: 梦哥，你来写！
    # 提示：先数 k 个节点，不够就返回 head
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
    print("K 个一组反转链表 - 测试用例")
    print("=" * 60)
    
    # 测试 1：k=2，一般情况
    print("\n【测试 1】k = 2")
    head = create_list([1, 2, 3, 4, 5])
    print(f"原始：", end="")
    print_list(head)
    result = reverse_k_group(head, 2)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：2 → 1 → 4 → 3 → 5 → None")
    
    # 测试 2：k=3
    print("\n【测试 2】k = 3")
    head = create_list([1, 2, 3, 4, 5])
    print(f"原始：", end="")
    print_list(head)
    result = reverse_k_group(head, 3)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：3 → 2 → 1 → 4 → 5 → None")
    
    # 测试 3：k=3，刚好整除
    print("\n【测试 3】k = 3，刚好整除")
    head = create_list([1, 2, 3, 4, 5, 6])
    print(f"原始：", end="")
    print_list(head)
    result = reverse_k_group(head, 3)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：3 → 2 → 1 → 6 → 5 → 4 → None")
    
    # 测试 4：k=1（不反转）
    print("\n【测试 4】k = 1（不反转）")
    head = create_list([1, 2, 3, 4, 5])
    print(f"原始：", end="")
    print_list(head)
    result = reverse_k_group(head, 1)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：1 → 2 → 3 → 4 → 5 → None（不变）")
    
    # 测试 5：k > 链表长度（不足 k 个，不变）
    print("\n【测试 5】k = 5，但只有 3 个节点")
    head = create_list([1, 2, 3])
    print(f"原始：", end="")
    print_list(head)
    result = reverse_k_group(head, 5)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：1 → 2 → 3 → None（不变）")
    
    # 测试 6：空链表
    print("\n【测试 6】空链表")
    head = create_list([])
    print(f"原始：", end="")
    print_list(head)
    result = reverse_k_group(head, 3)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望： → None（空）")
    
    # 测试 7：单个节点
    print("\n【测试 7】单个节点")
    head = create_list([1])
    print(f"原始：", end="")
    print_list(head)
    result = reverse_k_group(head, 2)
    print(f"结果：", end="")
    print_list(result)
    print(f"期望：1 → None（不变）")
    
    print("\n" + "=" * 60)
    print("练习完成！检查所有测试用例是否通过！")
    print("=" * 60)
