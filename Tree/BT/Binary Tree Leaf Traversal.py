from typing import List, Optional
from collections import defaultdict 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:  
    def _dfs(self, u: TreeNode, dp, ans):
        if not u: return 
        self._dfs(u.left, dp, ans)
        self._dfs(u.right, dp, ans) 
        dp[u] = 1 + max(dp[u.left], dp[u.right])
        ans[dp[u]].append(u.val) 

    def _dfs(self, u: TreeNode, ans):
        if not u: return 0 
        h = 1 + max(self._dfs(u.left, ans), self._dfs(u.right, ans))
        ans[h].append(u.val)
        return h
    
    def get_leaf(self, u: Optional[TreeNode]) -> List[int]: 
        dp = defaultdict(int)
        ans = defaultdict(list)
        # self._dfs(u, dp, ans)
        self._dfs(u, ans)

        return [v for _, v in ans.items()]

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
    u = build_BT([1,2,3,4,5])
    out = solution.get_leaf(u) 
    print(out)
if __name__ == "__main__":
    main()
