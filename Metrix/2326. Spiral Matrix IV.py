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
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        l, r, t, b = 0, n - 1, 0, m - 1

        cur = head
        while cur: # 模拟一个转圈
            for j in range(l, r + 1):
                if ans[t][j] != -1 or not cur: break 
                ans[t][j] = cur.val
                cur = cur.next  

            for i in range(t + 1, b + 1):
                if ans[i][r] != -1 or not cur: break 
                ans[i][r] = cur.val
                cur = cur.next 
 
            for j in range(r - 1, l - 1, -1):
                if ans[b][j] != -1 or not cur: break 
                ans[b][j] = cur.val
                cur = cur.next 
 
            for i in range(b - 1, t, -1): # 不碰到 t
                if ans[i][l] != -1 or not cur: break 
                ans[i][l] = cur.val
                cur = cur.next 

            l += 1
            r -= 1
            t += 1
            b -= 1
        return ans
    


    
def main():
    solution = Solution() 
    m = 3
    n = 5
    head_array = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
    head = array_to_linked_list(head_array)
    solution = Solution() 
    out = solution.spiralans(m, n, head) 
    print(out) 

if __name__ == "__main__":
    main()
