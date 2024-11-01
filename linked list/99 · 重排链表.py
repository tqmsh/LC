class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next: 'ListNode' = next
class Solution:
    def _mid(self, x: ListNode):
        s, f = x, x.next
        while f and f.next:
            s = s.next
            f = f.next.next
        return s
    def _rev(self, x: ListNode): # f -> e -> d -> None
        L = None 
        while x:  
            R = x.next  
            x.next = L;  # 重链 x  
            L = x; x = R
        return L
    def _merge(self, x: ListNode, y: ListNode):
        while y:
            R_x = x.next; R_y = y.next # x -> y -> x_R 
            x.next = y; y.next = R_x # 重链 x, y
            x = R_x; y = R_y   
    def reorderList(self, head: ListNode): 
        mid = self._mid(head) # a -> b -> c (mid) -> d -> e
        tmp = mid.next; mid.next = None # tmp = d -> e
        self._merge(head, self._rev(tmp)) # rev: e -> d -> None, len <= head -> mid
        return head
def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

def get_node_index(head, node):
    index = 0
    while head:
        if head == node:
            return index
        head = head.next
        index += 1
    return None

print_linked_list(Solution().reorderList(array_to_linked_list([1,2,3,4,5])))