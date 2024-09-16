from typing import List, Optional
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def _dfs(self, u: TreeNode, lvl_f, mp: defaultdict[int, deque]):
        if not u: return
        lvl_u = lvl_f + 1
        if lvl_u % 2: mp[lvl_u].append(u.val)
        else: mp[lvl_u].appendleft(u.val)
        # 如果是利用父亲结点信息计算，先递归父亲再计算
        self._dfs(u.left, lvl_u, mp)
        self._dfs(u.right, lvl_u, mp)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(deque)
        self._dfs(root, 0, mp)

        ans = []
        for k in mp.keys():  
            ans.append([x for x in mp[k]])
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
    root = build_BT([3, 9, 20, None, None, 15, 7])
    out = solution.zigzagLevelOrder(root) 
    print(out)
if __name__ == "__main__":
    main()
