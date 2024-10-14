class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next: 'ListNode' = next
class Solution:
    def _mid(self, x: ListNode):
        s, f = x, x
        while f and f.next:
            s = s.next
            f = f.next.next
        return s
    # a -> b -> c -> d -> e -> f

    # a -> b -> c -> d -> None
    #                ↑
    #                e  
    #                ↑
    #                f
    def _rev(self, x: ListNode):
        L = None
        while x:
            R = x.next
            x.next = L
            L = x
            x = R

    
    def reorder_list(self, head: ListNode):
        mid = self._mid(head)
        self._rev(mid)
        