#复习一下二叉树的基础代码

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinartTree:
    def __init__(self):
        self.root = None

    def preorder(self):
        result = self._preorder_helper(self.root)
        print(f"前序遍历：{' → '.join(map(str, result))}")
        return result
    
    def _preorder_helper(self, node):
        if node is None:
            return []
        else:
            return [node.val] + self._preorder_helper(node.left) + self._preorder_helper(node.right)   
        
    def inorder(self):
        result = self._inorder_helper(node)
        print(f"中序遍历：{' → '.join(map(str, result))}")    
        return result
    
    def _inorder_helper(node):
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
        if self.root is None:
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