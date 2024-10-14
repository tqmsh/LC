from typing import List, Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def _dfs(self, u: TreeNode, ans: List, mp: defaultdict[TreeNode, int]):
        if not u: 
            dp_u = ""
            return dp_u
        # 如果是利用儿子结点信息计算，先递归再计算  

        # dp1[u]: u 子树的 pre_order
        # dp1[u] = f'{u.val}, dp1[v_l], dp1[v_r]'
        dp1_v_l = self._dfs(u.left, ans, mp)
        dp1_v_r = self._dfs(u.right, ans, mp)
        dp_u = f'{u.val}, {dp1_v_l}, {dp1_v_r}'

        mp[dp_u] += 1
        if mp[dp_u] == 2: ans.append(u)

        return dp_u
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        mp = defaultdict(int)

        self._dfs(root, ans, mp)
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

def print_bst(node, level=0, label='.'):
    indent = '   ' * level
    if node is not None:
        print(f"{indent}-{label}: {node.val}")
        print_bst(node.left, level + 1, 'L')
        print_bst(node.right, level + 1, 'R')
    else:
        print(f"{indent}-{label}: None")


def main():
    solution = Solution()
    root = build_BT([1,2,3,4,None,2,4,None,None,4])

    out = solution.findDuplicateSubtrees(root) 
    for x in out:
        print_bst(x)
        
    print(out)
if __name__ == "__main__":
    main()
