# 🌳 练习 4 - 树的经典算法题

**难度**：⭐⭐⭐⭐  
**目标**：掌握树的经典面试算法题

---

## 📝 任务

补全以下经典算法题：

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_symmetric(root):
    """
    判断二叉树是否对称（镜像）
    
    示例：
    对称：          不对称：
      1               1
     / \             / \
    2   2           2   2
   / \             /     \
  3   3           3       3
  
    输出：True / False
    """
    # TODO: 补全代码
    pass


def max_depth(root):
    """
    计算二叉树的最大深度
    
    示例：
      1
     / \
    2   3
       / \
      4   5
    
    输出：3
    """
    # TODO: 补全代码
    pass


def min_depth(root):
    """
    计算二叉树的最小深度（从根到最近叶子节点的路径长度）
    
    注意：叶子节点是指没有子节点的节点！
    
    示例：
      1
     / \
    2   3
       / \
      4   5
    
    输出：2（路径 1→2）
    """
    # TODO: 补全代码
    pass


def invert_tree(root):
    """
    翻转二叉树（左右互换）
    
    示例：
    翻转前：        翻转后：
      4              4
     / \            / \
    2   7    →     7   2
   / \ / \        / \ / \
  1  3 6  9      9  6 3  1
  
    返回翻转后的根节点
    """
    # TODO: 补全代码
    pass


def lowest_common_ancestor(root, p, q):
    """
    找到两个节点的最近公共祖先（LCA）
    
    示例：
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
    
    LCA(5, 1) = 3
    LCA(5, 4) = 5
    
    返回最近公共祖先节点
    """
    # TODO: 补全代码
    pass


def build_tree_from_preorder_inorder(preorder, inorder):
    """
    根据前序和中序遍历结果重建二叉树
    
    示例：
    preorder = [3, 9, 20, 15, 7]
    inorder  = [9, 3, 15, 20, 7]
    
    重建的树：
        3
       / \
      9  20
        /  \
       15   7
    
    返回根节点
    """
    # TODO: 补全代码
    pass


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 测试对称树
    print("【对称树测试】")
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.right.right = TreeNode(3)
    print(f"对称树：{is_symmetric(root1)} (期望：True)")
    
    # 测试最大深度
    print("\n【最大深度测试】")
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    print(f"最大深度：{max_depth(root2)} (期望：3)")
    
    # 测试最小深度
    print("\n【最小深度测试】")
    print(f"最小深度：{min_depth(root2)} (期望：2)")
    
    # 测试翻转树
    print("\n【翻转树测试】")
    root3 = TreeNode(4)
    root3.left = TreeNode(2)
    root3.right = TreeNode(7)
    root3.left.left = TreeNode(1)
    root3.left.right = TreeNode(3)
    root3.right.left = TreeNode(6)
    root3.right.right = TreeNode(9)
    
    inverted = invert_tree(root3)
    print(f"翻转后左子节点：{inverted.left.val} (期望：7)")
    print(f"翻转后右子节点：{inverted.right.val} (期望：2)")
    
    print("\n✅ 完成！")
```

---

## 💡 提示

1. **对称树**：比较左子树的左和右子树的右，左子树的右和右子树的左
2. **最大深度**：`1 + max(左深度，右深度)`
3. **最小深度**：注意只有单侧子树的情况！
4. **翻转树**：递归交换左右子节点
5. **LCA**：递归，如果 p、q 分别在左右子树，当前节点就是 LCA
6. **重建树**：前序第一个是根，用它在 inorder 中分割左右子树

---

## 🎯 这些题很重要！

这些都是 LeetCode 经典题目，面试经常出现：
- 104. 二叉树的最大深度
- 111. 二叉树的最小深度
- 226. 翻转二叉树
- 101. 对称二叉树
- 236. 二叉树的最近公共祖先
- 105. 从前序与中序遍历序列构造二叉树

---

## ✅ 验证

运行后输出应该与期望值一致！
