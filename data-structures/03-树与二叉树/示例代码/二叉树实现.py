# 二叉树完整实现
# 梦哥，先理解这个，再去做练习！

class TreeNode:
    """二叉树节点"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    """二叉搜索树"""
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        """判断是否为空"""
        return self.root is None
    
    def insert(self, val):
        """插入节点（BST 规则：左<根<右）"""
        if self.root is None:
            self.root = TreeNode(val)
            print(f"✓ 插入根节点：{val}")
        else:
            self._insert_helper(self.root, val)
    
    def _insert_helper(self, node, val):
        """递归插入"""
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
                print(f"✓ 插入 {val} 到 {node.val} 的左子节点")
            else:
                self._insert_helper(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
                print(f"✓ 插入 {val} 到 {node.val} 的右子节点")
            else:
                self._insert_helper(node.right, val)
    
    def search(self, val):
        """查找元素"""
        result = self._search_helper(self.root, val)
        if result:
            print(f"✓ 找到：{val}")
        else:
            print(f"✗ 未找到：{val}")
        return result
    
    def _search_helper(self, node, val):
        """递归查找"""
        if node is None:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._search_helper(node.left, val)
        else:
            return self._search_helper(node.right, val)
    
    def delete(self, val):
        """删除节点"""
        self.root = self._delete_helper(self.root, val)
    
    def _delete_helper(self, node, val):
        """递归删除（三种情况）"""
        if node is None:
            print(f"✗ 未找到：{val}")
            return None
        
        if val < node.val:
            node.left = self._delete_helper(node.left, val)
        elif val > node.val:
            node.right = self._delete_helper(node.right, val)
        else:
            # 找到要删除的节点
            print(f"✓ 删除：{val}")
            
            # 情况 1：叶子节点
            if node.left is None and node.right is None:
                return None
            
            # 情况 2：只有一个子节点
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # 情况 3：有两个子节点
            # 找右子树的最小值（中序后继）
            min_node = self._find_min(node.right)
            node.val = min_node.val
            node.right = self._delete_helper(node.right, min_node.val)
        
        return node
    
    def _find_min(self, node):
        """找最小值节点"""
        current = node
        while current.left:
            current = current.left
        return current
    
    # ==================== 遍历方法 ====================
    
    def preorder(self):
        """前序遍历：根→左→右"""
        result = self._preorder_helper(self.root)
        print(f"前序遍历：{' → '.join(map(str, result))}")
        return result
    
    def _preorder_helper(self, node):
        if node is None:
            return []
        return [node.val] + self._preorder_helper(node.left) + self._preorder_helper(node.right)
    
    def inorder(self):
        """中序遍历：左→根→右（BST 中序是有序的！）"""
        result = self._inorder_helper(self.root)
        print(f"中序遍历：{' → '.join(map(str, result))}")
        return result
    
    def _inorder_helper(self, node):
        if node is None:
            return []
        return self._inorder_helper(node.left) + [node.val] + self._inorder_helper(node.right)
    
    def postorder(self):
        """后序遍历：左→右→根"""
        result = self._postorder_helper(self.root)
        print(f"后序遍历：{' → '.join(map(str, result))}")
        return result
    
    def _postorder_helper(self, node):
        if node is None:
            return []
        return self._postorder_helper(node.left) + self._postorder_helper(node.right) + [node.val]
    
    def level_order(self):
        """层序遍历（BFS）"""
        if self.root is None:
            print("层序遍历：树为空")
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        print(f"层序遍历：{' → '.join(map(str, result))}")
        return result
    
    def get_height(self):
        """获取树的高度"""
        height = self._get_height_helper(self.root)
        print(f"树的高度：{height}")
        return height
    
    def _get_height_helper(self, node):
        if node is None:
            return 0
        return 1 + max(self._get_height_helper(node.left), self._get_height_helper(node.right))
    
    def get_size(self):
        """获取节点数量"""
        size = self._get_size_helper(self.root)
        print(f"节点数量：{size}")
        return size
    
    def _get_size_helper(self, node):
        if node is None:
            return 0
        return 1 + self._get_size_helper(node.left) + self._get_size_helper(node.right)
    
    def display_tree(self):
        """可视化打印树（缩进式）"""
        self._display_helper(self.root, 0)
    
    def _display_helper(self, node, level):
        if node is None:
            return
        self._display_helper(node.right, level + 1)
        print("    " * level + f"├── {node.val}")
        self._display_helper(node.left, level + 1)


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("二叉树操作演示")
    print("=" * 60)
    
    # 创建二叉搜索树
    bst = BinaryTree()
    
    # 插入节点
    print("\n【插入节点】")
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    
    # 可视化树
    print("\n【树的结构】")
    bst.display_tree()
    
    # 查找
    print("\n【查找】")
    bst.search(40)
    bst.search(100)
    
    # 四种遍历
    print("\n【遍历】")
    bst.preorder()
    bst.inorder()
    bst.postorder()
    bst.level_order()
    
    # 树的属性
    print("\n【树的属性】")
    bst.get_height()
    bst.get_size()
    
    # 删除节点
    print("\n【删除节点】")
    print("删除 20（叶子节点）:")
    bst.delete(20)
    bst.display_tree()
    
    print("\n删除 30（有一个子节点）:")
    bst.delete(30)
    bst.display_tree()
    
    print("\n删除 50（根节点，有两个子节点）:")
    bst.delete(50)
    bst.display_tree()
    
    # 验证中序遍历仍然有序
    print("\n【删除后验证】")
    bst.inorder()
    
    print("\n" + "=" * 60)
    print("✅ 演示完成！")
    print("=" * 60)
