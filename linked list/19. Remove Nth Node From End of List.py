from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  
        ans = ListNode(0, head); s = ans; f = head # 0 (s) -> 1 -> 2 -> 3 (f)-> 4 -> 5
                                                   # 0 -> 1 -> 2 -> 3 (s) -> 4 -> 5 -> x (f)

                                                   # edge case
                                                   # 0 (s) -> 1 -> x (f)
                                                   # => None
        for i in range(n):
            f = f.next

        while f: 
            f = f.next
            s = s.next

        s.next = s.next.next 
        return ans.next
 
def main():
    solution = Solution() 
    head = solution.removeNthFromEnd(array_to_linked_list([1]), 1) 
    print_linked_list(head)

if __name__ == "__main__":
    main()
