import gc
class ListNode:
    def __init__(self, val=0, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre 
class DLL:
    def __init__(self):
        self.head = None

    # Merge Sort
    def _split(self, node: ListNode):
        s = f = node
        while f and f.next and f.next.next:
            f = f.next.next
            s = s.next
        ans = s.next # s: mid; s,nxt: 后半段开头
        s.next = None
        return ans
    def _merge(self, fir, sec): 
        if not fir: return sec
        if not sec: return fir
        if fir.val > sec.val: fir, sec = sec, fir # wlog, fir <= sec
        fir.next = self._merge(fir.next, sec)
        fir.next.pre = fir
        fir.pre = None
        return fir 
    def _merge_sort(self, fir):
        if fir is None or fir.next is None: return fir 
        sec = self._split(fir)
        fir = self._merge_sort(fir)
        sec = self._merge_sort(sec) 
        return self._merge(fir, sec)
    def sort(self):
        self.head = self._merge_sort(self.head)
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
            print(node.val, end=" -> ")
            node = node.next
        print("None")


dll = DLL()
for value in [2, 1,1,2,3,4,4,1]:
    dll.insert_end(value)
dll.sort()
dll.display_list(dll.head) 
