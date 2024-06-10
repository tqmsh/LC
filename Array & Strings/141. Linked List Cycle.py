from typing import Optional
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s, f = head

        # 链表 查环 模版
        while (f and f.next):
            f = f.next.next
            s = s.next

            if s == f:  
                return True
        
        return False
    

def main():
    solution = Solution()

    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4) 
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1
    
    out = solution.hasCycle(node1)
    print(out) 

if __name__ == "__main__":
    main()
