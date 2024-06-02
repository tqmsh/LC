from typing import Optional 
import random
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.x = head     

    def getRandom(self) -> int:
        a = []
        cur = self.x
        while cur: 
            a += [cur.val]
            cur = cur.next  
        
        # random 模版
        return random.choice(a)
def main(): 
    head = array_to_linked_list([1, 2, 3])
    solution = Solution(head)
    print(solution.getRandom())
      
if __name__ == "__main__":
    main()
