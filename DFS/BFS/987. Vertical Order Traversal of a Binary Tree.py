from typing import List 
from typing import Optional 
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    
    def _dfs(self, u: TreeNode, x, y, mp):
        if not u: return
        mp[y].append((x, u.val))
        self._dfs(u.left, x + 1, y - 1, mp)
        self._dfs(u.right, x + 1, y + 1, mp)
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:      
        mp = defaultdict(list); ans = []
        self._dfs(root, 0, 0, mp)
        for k in sorted(mp.keys()): # 按列排
            mp[k].sort() # 按行, 值徘
            ans.append([x for _, x in mp[k]])
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
    root = build_BT([1,2,3,4,5,6,7])
    out = solution.verticalTraversal(root) 
    print(out)
if __name__ == "__main__":
    main()
