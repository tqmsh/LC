from typing import List 
from typing import Optional
 
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

class Solution:
    def getDecimalValue(self, head: ListNode) -> int: 
        ans = ''
        cur = head
        while cur: 
            ans += str(cur.val)
            cur = cur.next  
        # 进制转换 模版
        return int(ans, 2)
    
def main():
    solution = Solution() 
    head = [1,0,1]
    head = array_to_linked_list(head)
    solution = Solution() 
    out = solution.getDecimalValue(head) 
    print(out) 

if __name__ == "__main__":
    main()
