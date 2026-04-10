class TreeNode:
    """二叉树节点：存储数据和左右子节点指针"""
    def __init__(self, val):
        self.val = val      # val = value，节点存储的值
        self.left = None    # 左子节点，默认为空
        self.right = None   # 右子节点，默认为空


class BinaryTree:
    """二叉搜索树（BST）：左子树 < 根 < 右子树"""
    
    def __init__(self):
        self.root = None    # 根节点，初始化为空

    # 插入（二叉搜索树规则）
    def insert(self, val):
        """
        插入新值的对外接口
        _  开头的函数表示"私有"，外部不需要直接调用
        """
        if self.root is None:  # 如果树是空的，直接创建根节点
            self.root = TreeNode(val) 
        else:  # 其他情况，交给递归函数处理
            # ✅ 注意：是 self.root，不是 node.root！
            # ValueError 是个错误，完全不该传入！
            self._insert_helper(self.root, val)

    # 使用了递归法插入新节点
    def _insert_helper(self, node, val):
        """
        递归插入的辅助函数
        node: 当前检查的节点
        val: 要插入的值
        """
        if val < node.val:  # ✅ 比较大小是为了保持 BST 规则：左小右大
            if node.left is None:  # 左子节点为空，就在这里插入
                node.left = TreeNode(val)
            else:  # 左子节点已有，继续往左子树里找空位
                self._insert_helper(node.left, val)
        else:  # val >= node.val，塞到右边
            if node.right is None:
                # ✅ 注意：node.right（点号），不是 node,right（逗号）！
                node.right = TreeNode(val)
            else:
                self._insert_helper(node.right, val)
    
    # 查找
    def search(self, val):
        """查找某个值是否存在，返回 True/False"""
        return self._search_helper(self.root, val)
    
    def _search_helper(self, node, val):
        """递归查找辅助函数"""
        # ✅ 注意：None 首字母大写！none 是未定义变量
        if node is None:  
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._search_helper(node.left, val)
        else:
            return self._search_helper(node.right, val)
    
    # 前序遍历（根→左→右） 
    def preorder(self, node):
        """前序遍历：先访问根，再遍历左子树，最后遍历右子树"""
        if node is None:
            return []
        return [node.val] + self.preorder(node.left) + self.preorder(node.right)
        # ✅ 你总结得很对！二叉树的确很多地方都用递归
        # 递归：天才的设计！用"已经可以"来解决"还没解决"

    # 中序遍历（左→根→右）- BST 中序是有序的！
    def inorder(self, node):
        """中序遍历：先遍历左子树，再访问根，最后遍历右子树"""
        if node is None:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

    # 后序遍历（左→右→根）
    def postorder(self, node):
        """后序遍历：先遍历左子树，再遍历右子树，最后访问根"""
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.val]


    # 层序遍历（BFS）- 一层一层地遍历
    def level_order(self):
        """
        层序遍历：用队列实现，一层一层从左到右遍历
        队列（queue）就像排队付款：先来的人先付款（FIFO）
        """
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]  # 队列初始化为根节点
        
        # 当队列不为空时，持续处理
        while queue:
            # 取出队首元素（最先进入的）
            node = queue.pop(0)  
            result.append(node.val)  # 记录当前节点的值
            
            # 把当前节点的左右子节点加入队尾
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 创建一棵树
    tree = BinaryTree()
    
    # 插入一些值（BST 会自动按规则排列）
    for val in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(val)
    
    # 查找
    print(f"查找 4: {tree.search(4)}")       # True
    print(f"查找 10: {tree.search(10)}")     # False
    
    # 遍历
    print(f"前序遍历: {tree.preorder(tree.root)}")  # [5, 3, 2, 4, 7, 6, 8]
    print(f"中序遍历: {tree.inorder(tree.root)}")   # [2, 3, 4, 5, 6, 7, 8] - BST 中序是有序的！
    print(f"后序遍历: {tree.postorder(tree.root)}")  # [2, 4, 3, 6, 8, 7, 5]
    print(f"层序遍历: {tree.level_order()}")        # [5, 3, 7, 2, 4, 6, 8]
