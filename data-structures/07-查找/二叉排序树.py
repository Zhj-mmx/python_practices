class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

#算法7.4 二叉排序树的查找
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.data == key:
            return node
        if key < node.data:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

#算法7.5 二叉排序树的插入

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

#算法7.6 二叉排序树的创建
    def create_bst(self):
        e = ElemType(input())
        while e.key != ENDFLAG:
            self.insert_bst(e)
            e = ElemType(input())

#算法7.7 二叉排序树的删除
    def delete_bst(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.data:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)
        return node
