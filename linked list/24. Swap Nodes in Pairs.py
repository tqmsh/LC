from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 双指针
        s, f = head, head 
        if f and f.next: f = f.next #🟥整套防护，防[]
        # 走到头 
        while f and f.next and f.next.next:
            f.val, s.val = s.val, f.val 
            f = f.next.next
            s = s.next.next 

        if f and s: f.val, s.val = s.val, f.val 
        return head 
    
def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    xrent = head
    for value in arr[1:]:
        xrent.next = ListNode(value)
        xrent = xrent.next
    return head

def print_linked_list(head):
    xrent = head
    while xrent:
        print(xrent.val, end=" -> " if xrent.next else "\n")
        xrent = xrent.next

def main():
    solution = Solution()
    head = array_to_linked_list([1,2,3,4])
    
    out = solution.swapPairs(head) 
    print_linked_list(out)

if __name__ == "__main__":
    main()
