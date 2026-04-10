# 🌳 练习 3 - 层序遍历与树的深度

**难度**：⭐⭐⭐  
**目标**：掌握 BFS 和树的相关计算

---

## 📝 任务

补全以下函数：

```python
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order(root):
    """
    层序遍历（BFS）
    
    示例：
        1
       / \
      2   3
     / \
    4   5
    
    输出：[1, 2, 3, 4, 5]
    """
    if root is None:
        return []
    
    # TODO: 使用队列实现层序遍历
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        # TODO: 将左右子节点加入队列
        pass
    
    return result


def level_order_by_level(root):
    """
    按层返回（每层一个列表）
    
    示例：
        1
       / \
      2   3
     / \
    4   5
    
    输出：[[1], [2, 3], [4, 5]]
    """
    if root is None:
        return []
    
    # TODO: 补全代码
    pass


def get_depth(root):
    """
    计算树的最大深度
    
    示例：
        1
       / \
      2   3
     / \
    4   5
    
    输出：3
    """
    # TODO: 用递归实现
    pass


def is_complete_binary_tree(root):
    """
    判断是否是完全二叉树
    
    完全二叉树：除了最后一层，其他层都填满；最后一层从左到右连续
    
    示例：
    完全二叉树：       不是完全二叉树：
        1                   1
       / \                 / \
      2   3               2   3
     / \                 /   /
    4   5               4   5
    
    输出：True / False
    """
    if root is None:
        return True
    
    # TODO: 使用层序遍历的思想
    # 提示：遇到第一个空节点后，后面不应该再有非空节点
    pass


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 构建测试树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("层序遍历:", level_order(root))
    print("期望：   [1, 2, 3, 4, 5]")
    
    print("\n按层返回:", level_order_by_level(root))
    print("期望：   [[1], [2, 3], [4, 5]]")
    
    print("\n树的深度:", get_depth(root))
    print("期望：   3")
    
    print("\n是否完全二叉树:", is_complete_binary_tree(root))
    print("期望：   True")
```

---

## 💡 提示

1. **层序遍历**：使用队列（deque），先进先出
2. **按层返回**：记录每层的节点数量，一次处理一层
3. **深度计算**：递归，`1 + max(左深度，右深度)`
4. **完全二叉树**：层序遍历，遇到第一个 None 后，后面不能有非 None 节点

---

## ✅ 验证

运行后输出应该与期望值一致！
