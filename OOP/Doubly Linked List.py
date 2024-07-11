import gc
class ListNode:
    def __init__(self, val=0, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_front(self, val):
        node = ListNode(val)
        node.next = self.head
        if self.head: self.head.pre = node # node <-> head
        self.head = node 
    def insert_after(self, L, val):
        node = ListNode(val) 
        if L: node.next = L.next  # node <-> R
        if node.next: node.next.pre = node 
        if L: L.next = node # L <-> node
        node.prev = L  
    def insert_end(self, val):
        node = ListNode(val)
        if not self.head: 
            self.head = node # empty
            return 
        tmp = self.head
        while tmp.next: tmp = tmp.next # 走到最后
        tmp.next = node # tmp <-> node
        node.pre = tmp
    def delete_node(self, delete_node):
        if not self.head or not delete_node: return
        if delete_node == self.head: self.head = delete_node.next 
        if delete_node.pre: delete_node.pre.next = delete_node.next # L <-> delete_node <-> R => L <-> R
        if delete_node.next: delete_node.next.pre = delete_node.pre
        gc.collect # free memory
    def display_list(self, node):
        while node:
            print(node.val, end = " -> ")
            L = node
            node = node.next 
 
d_linked_list = DoublyLinkedList() 
d_linked_list.insert_end(5)
d_linked_list.insert_front(1)
d_linked_list.insert_front(6)
d_linked_list.insert_end(9)  
d_linked_list.insert_after(d_linked_list.head, 11) 
d_linked_list.insert_after(d_linked_list.head.next, 15) 
d_linked_list.display_list(d_linked_list.head) 
d_linked_list.delete_node(d_linked_list.head.next.next.next.next.next) 
d_linked_list.display_list(d_linked_list.head)