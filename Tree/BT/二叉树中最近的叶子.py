from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _dfs(self, u, f, k, fa): 
        fa[u] = f 
        if u.val == k: return u
        if u.left: return self._dfs(u.left, u, k, fa)
        if u.right: return self._dfs(u.right, u, k, fa) 
        
    def closest_leaf(self, root: Optional[TreeNode], k: int):
        fa = {}
        k = self._dfs(root, None, k, fa)
        q = [k]
        vis = set([k]) 
        while q:
            now = q.pop(0)
            if now.left is None and now.right is None: return now.val 
            if now.left and now.left not in vis: 
                q.append(now.left)
                vis.add(now.left)
            if now.right and now.right not in vis:
                q.append(now.right)
                vis.add(now.right)
            nxt = fa[now]
            if nxt and nxt not in vis:
                q.append(nxt)
                vis.add(nxt)
            
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
    root = build_BT([1,3,2])
    k = 1
    out = solution.closest_leaf(root, k) 
    print(out)
if __name__ == "__main__":
    main()
