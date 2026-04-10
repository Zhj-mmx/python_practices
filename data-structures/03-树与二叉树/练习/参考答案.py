# 🌳 练习参考答案

**梦哥，做完练习再看答案哦！**

---

## 练习 1 - 二叉树遍历

```python
def preorder(root):
    """前序遍历：根 → 左 → 右"""
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    """中序遍历：左 → 根 → 右"""
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    """后序遍历：左 → 右 → 根"""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

---

## 练习 2 - 二叉搜索树

```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert_helper(self.root, val)
    
    def _insert_helper(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_helper(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_helper(node.right, val)
    
    def search(self, val):
        return self._search_helper(self.root, val)
    
    def _search_helper(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._search_helper(node.left, val)
        else:
            return self._search_helper(node.right, val)
    
    def get_min(self):
        if self.root is None:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.val
    
    def get_max(self):
        if self.root is None:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.val
    
    def get_height(self):
        return self._get_height_helper(self.root)
    
    def _get_height_helper(self, node):
        if node is None:
            return 0
        return 1 + max(self._get_height_helper(node.left), self._get_height_helper(node.right))
```

---

## 练习 3 - 层序遍历与深度

```python
from collections import deque


def level_order(root):
    """层序遍历"""
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


def level_order_by_level(root):
    """按层返回"""
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


def get_depth(root):
    """计算深度"""
    if root is None:
        return 0
    return 1 + max(get_depth(root.left), get_depth(root.right))


def is_complete_binary_tree(root):
    """判断完全二叉树"""
    if root is None:
        return True
    
    queue = deque([root])
    encountered_none = False
    
    while queue:
        node = queue.popleft()
        
        if node is None:
            encountered_none = True
        else:
            if encountered_none:
                return False
            queue.append(node.left)
            queue.append(node.right)
    
    return True
```

---

## 练习 4 - 树的算法题

```python
def is_symmetric(root):
    """判断对称树"""
    def is_mirror(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val and 
                is_mirror(t1.left, t2.right) and 
                is_mirror(t1.right, t2.left))
    
    return is_mirror(root, root) if root else True


def max_depth(root):
    """最大深度"""
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def min_depth(root):
    """最小深度"""
    if root is None:
        return 0
    
    # 只有右子树
    if root.left is None:
        return 1 + min_depth(root.right)
    # 只有左子树
    if root.right is None:
        return 1 + min_depth(root.left)
    # 两边都有
    return 1 + min(min_depth(root.left), min_depth(root.right))


def invert_tree(root):
    """翻转二叉树"""
    if root is None:
        return None
    
    # 交换左右子节点
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def lowest_common_ancestor(root, p, q):
    """最近公共祖先"""
    if root is None or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    return left if left else right


def build_tree_from_preorder_inorder(preorder, inorder):
    """重建树"""
    if not preorder or not inorder:
        return None
    
    # 前序第一个是根
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    # 在 inorder 中找到根的位置
    root_idx = inorder.index(root_val)
    
    # 递归构建左右子树
    root.left = build_tree_from_preorder_inorder(
        preorder[1:root_idx + 1], 
        inorder[:root_idx]
    )
    root.right = build_tree_from_preorder_inorder(
        preorder[root_idx + 1:], 
        inorder[root_idx + 1:]
    )
    
    return root
```

---

## 🎯 关键要点总结

1. **遍历是基础** - 前中后序 + 层序，必须熟练
2. **递归思维** - 树的问题大多可以用递归解决
3. **分解问题** - 把大问题分解为左子树 + 右子树
4. **边界条件** - 空节点（None）的处理很重要

---

加油梦哥！🌳
