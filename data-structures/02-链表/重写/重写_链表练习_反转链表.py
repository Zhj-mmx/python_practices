class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 迭代法反转链表
def reverse_iterative(head): #head作为链表的头指针，用来指示链表本身
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev #反转一次指针方向
        prev = current
        current = next_node #俩指针向后移
    return prev #反转后的链表以prev为头指针，故返回prev

# 递归法
def reverse_recursive(head):
    # 基础情况：空链表或只有一个节点
    # 很多递归法的使用都需要考虑到基础的情况
    if not head or not head.next:
        return head
    
    #递归的核心，将函数本身当作已经有的函数使用
    new_head = reverse_recursive(head.next) #将下一层链表反转

    head.next.next = head #下一层链表的指针指向自身
    head.next = None #反转自身的指针

    return new_head #new_head 就是反转后的头指针
    
