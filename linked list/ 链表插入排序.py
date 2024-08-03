from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertion_sort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        i = head 
        while i: # 目前
            R = i.next
 
            j = ans # 在已经排好的里面找介入点
            while j and j.next and j.next.val < i.val: j = j.next 
            i.next = j.next
            j.next = i
            
            i = R
        return ans.next
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
    head = array_to_linked_list([1,3,2,0])
    
    out = solution.insertion_sort(head) 
    print_linked_list(out)

if __name__ == "__main__":
    main()
