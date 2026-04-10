# 🌳 练习 1 - 二叉树基础遍历

**难度**：⭐⭐  
**目标**：掌握三种递归遍历方式

---

## 📝 任务

补全以下代码中的三种遍历方法：

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    """
    前序遍历：根 → 左 → 右
    
    示例：
        1
       / \
      2   3
     输出：[1, 2, 3]
    """
    # TODO: 补全代码
    pass


def inorder(root):
    """
    中序遍历：左 → 根 → 右
    
    示例：
        1
       / \
      2   3
     输出：[2, 1, 3]
    """
    # TODO: 补全代码
    pass


def postorder(root):
    """
    后序遍历：左 → 右 → 根
    
    示例：
        1
       / \
      2   3
     输出：[2, 3, 1]
    """
    # TODO: 补全代码
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
    
    print("前序遍历:", preorder(root))
    print("期望：  [1, 2, 4, 5, 3]")
    
    print("\n中序遍历:", inorder(root))
    print("期望：  [4, 2, 5, 1, 3]")
    
    print("\n后序遍历:", postorder(root))
    print("期望：  [4, 5, 2, 3, 1]")
```

---

## 💡 提示

1. **前序**：先访问根，再递归左子树，最后递归右子树
2. **中序**：先递归左子树，再访问根，最后递归右子树
3. **后序**：先递归左子树，再递归右子树，最后访问根

---

## ✅ 验证

运行后输出应该与期望值一致！
