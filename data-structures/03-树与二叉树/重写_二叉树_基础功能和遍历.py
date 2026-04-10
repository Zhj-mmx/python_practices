class TreeNode: #定义节点
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None

    # 插入（二叉搜索树规则）
    def insert(self, val):
        if self.root is None: #检查根是否存在
            self.root = TreeNode(val) 
        else: #其他情况打包给函数self._insert_helper()  ?为什么这样做？
            #↑的解答：insert() 是对外的接口，负责简单检查（树是否为空）
            #_insert_helper() 是内部递归实现，专注于"找到位置插入"
            #这是常见的编程模式：对外简洁，对内灵活
            self._insert_helper(self.root, val) 
            

    #使用了递归法插入新节点
    def _insert_helper(self, node, val):
        if val < node.val: #？为什么要比较节点大小？解答:规则：左子树 < 根 <= 右子树
            if node.left is None:
                node.left = TreeNode(val) #节点为空就添加
            else:
                self._insert_helper(node.left, val) #继续看下一个节点能不能添加
        else:
            if node.right is None: #和左边的情况一样
                node.right = TreeNode(val)
            else:
                self._insert_helper(node.right, val)
    # 查找
    def search(self, val):
        return self._search_helper(self.root, val)
    
    def _seacher_helper(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._seacher_helper(node.left, val)
        else:
            return self._seacher_helper(node.right, val)
    
    # 前序遍历（根→左→右） 
    def preorder(self, node):
        if node is None:
            return []
        return [node.val] + self.preorder(node.left) + self.preorder(node.right)
        # 又用了递归法，感觉二叉树里面好多地方适用递归法
        # 但不得不感慨递归真是天才的设计

    # 中序遍历（左→根→右）- BST 中序是有序的！
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)
        # val 是 value的简写吗？
    # 后序遍历（左→右→根）
    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.val]


    # 层序遍历（BFS） ?需要更仔细的讲解
    def level_order(self):
        if self.root is None:
            return []
        
        result = []
        queue = [self.root] # ？queue是怎么发挥作用的？回答:FIFO（先进先出）

        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
