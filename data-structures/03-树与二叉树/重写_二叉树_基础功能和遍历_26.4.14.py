class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
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
                node.left = val
            else:
                self._insert_helper(self.root, val)
        else:
            if node.right is None:
                node.right = val
            else:
                self._insert_helper(self.root, val)

    def search(self, val):
        return self._search_helper(self.root, val)
    
    def _search_helper(self, node, val):
        if node is none:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return selg._search_helper(node.left, val)
        else:
            return self._search_helper(node.right, val)

    # 前序遍历（根→左→右） 又叫先序遍历    
    def preorder(self, node):
        if node is None:
            return []
        return [node.val] + self.preorder(node.left) +self.preorder(node.right)
    
    # 中序遍历（左→根→右）- BST 中序是有序的！
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)

    # 后序遍历（左→右→根）
    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.val]    

    def level_order(self):
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]

        while queue:
            node = queue.pop[0]
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    

