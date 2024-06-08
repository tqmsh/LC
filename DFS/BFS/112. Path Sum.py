from typing import List 
from typing import Optional 
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: 
        global ans
        ans = 0
        
        def dfs(u, f, sum):  
            global ans
            if not u: 
                if not f.left and not f.right and sum == targetSum: ans = 1 
                return   
            dfs(u.left, u, sum + u.val)
            dfs(u.right, u, sum + u.val)  

        # 🟥特判，空 []
        if root == None: return 0
        
        dfs(root, -1, 0) 

        # bfs
        ans = 0
        q = deque([(root, -1, 0)])  
        def bfs():
            global ans
            while q:
                u, f, sum = q.popleft()
                if not u: 
                    if not f.left and not f.right and sum == targetSum: ans = 1 
                    continue   
                     
                q.append((u.left, u, sum + u.val))
                q.append((u.right, u, sum + u.val)) 
        if root == None: return 0
        bfs()
        return ans 
def build_BT(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        current = queue.pop(0)
        if arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    return root

def main():
    solution = Solution()
    root = [1,2]; targetSum = 3
    root = build_BT(root)
    out = solution.hasPathSum(root, targetSum) 
    print(out)
if __name__ == "__main__":
    main()
