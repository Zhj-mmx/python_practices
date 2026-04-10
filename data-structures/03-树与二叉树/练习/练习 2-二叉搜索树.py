# 🌳 练习 2 - 实现二叉搜索树（BST）

**难度**：⭐⭐⭐  
**目标**：掌握 BST 的插入、查找、删除操作

---

## 📝 任务

补全二叉搜索树的完整实现：

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """
        插入节点（BST 规则：左子树 < 根 < 右子树）
        """
        # TODO: 补全代码
        pass
    
    def _insert_helper(self, node, val):
        """递归插入辅助函数"""
        # TODO: 补全代码
        pass
    
    def search(self, val):
        """
        查找元素，存在返回 True，否则返回 False
        """
        # TODO: 补全代码
        pass
    
    def _search_helper(self, node, val):
        """递归查找辅助函数"""
        # TODO: 补全代码
        pass
    
    def get_min(self):
        """
        返回树中的最小值
        """
        # TODO: 补全代码
        pass
    
    def get_max(self):
        """
        返回树中的最大值
        """
        # TODO: 补全代码
        pass
    
    def get_height(self):
        """
        返回树的高度
        """
        # TODO: 补全代码
        pass
    
    def _get_height_helper(self, node):
        """递归计算高度"""
        # TODO: 补全代码
        pass


# ==================== 测试代码 ====================
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # 插入测试
    print("【插入测试】")
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    print("插入：50, 30, 70, 20, 40, 60, 80")
    
    # 查找测试
    print("\n【查找测试】")
    print(f"查找 40: {bst.search(40)} (期望：True)")
    print(f"查找 100: {bst.search(100)} (期望：False)")
    
    # 最值测试
    print("\n【最值测试】")
    print(f"最小值：{bst.get_min()} (期望：20)")
    print(f"最大值：{bst.get_max()} (期望：80)")
    
    # 高度测试
    print("\n【高度测试】")
    print(f"树的高度：{bst.get_height()} (期望：3)")
```

---

## 💡 提示

1. **BST 规则**：左子树所有节点 < 根节点 < 右子树所有节点
2. **插入**：从根开始比较，小于当前节点往左，大于往右，找到空位插入
3. **查找**：类似插入，找到值返回 True，遇到 None 返回 False
4. **最小值**：一直往左走到底
5. **最大值**：一直往右走到底
6. **高度**：`1 + max(左子树高度，右子树高度)`

---

## 🎯 扩展挑战（选做）

实现 `delete(val)` 方法删除节点，需要考虑三种情况：
1. 叶子节点 - 直接删除
2. 只有一个子节点 - 用子节点替代
3. 有两个子节点 - 用右子树的最小值（或左子树的最大值）替代

---

## ✅ 验证

所有测试输出应该与期望值一致！
