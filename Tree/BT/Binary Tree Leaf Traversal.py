from typing import List, Optional
from collections import defaultdict 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:  
    def _dfs(self, u: TreeNode, path: int, ans: int) -> int:
        if not u: return
        
        current_path = path * 10 + u.val
        # 进门前处理，因为得用 f 的信息分类讨论
        if u.left is None and u.right is None:
            ans[0] += current_path
            return 
            
        self._dfs(u.left, current_path, ans)
        self._dfs(u.right, current_path, ans) 
    
    def sumNumbers(self, u: Optional[TreeNode]) -> List[int]: 
        ans = [0] 
        self._dfs(u, 0, ans)
        return ans[0]

def build_BT(arr):
    if not arr:
        return None
    u = TreeNode(arr[0])
    queue = [u]
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
    return u

def main():
    solution = Solution()
    u = build_BT([4,9,0,None,1])
    out = solution.sumNumbers(u) 
    print(out)
if __name__ == "__main__":
    main()
