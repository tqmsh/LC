from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
class Solution:
    def _dfs(self, u, dp):
        if not u: return
        dp[(u, 1)] = u.val
        dp[(u, 0)] = 0
        if u.left:
            self._dfs(u.left, dp)
            dp[(u, 0)] += max(dp[(u.left, 0)], dp[(u.left, 1)])
            dp[(u, 1)] += dp[(u.left, 0)]

        if u.right:
            self._dfs(u.right, dp)
            dp[(u, 0)] += max(dp[(u.right, 0)], dp[(u.right, 1)])
            dp[(u, 1)] += dp[(u.right, 0)]

    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        self._dfs(root, dp)
        return max(dp[(root, 0)], dp[(root, 1)])
    
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
    root = build_BT([3,4,5,1,3,None,1])
    out = solution.rob(root) 
    print(out)
if __name__ == "__main__":
    main()
