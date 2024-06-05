from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
# 🟥如果要拿 L, R 东西 (val)的话，得判断，否则不用
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # f[i][j]: i, j 子树是否镜面对称
        def dfs(rt1, rt2):
            # 基
            if not rt1 and not rt2: return 1
            if not (rt1 and rt2): return 0

            ans = 1
            if rt1.val != rt2.val: ans = 0
            if not dfs(rt1.right, rt2.left): ans = 0
            if not dfs(rt1.left, rt2.right): ans = 0
            
            return ans
        
        return dfs(root, root) 
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
    root = build_BT([1,2,2])
    out = solution.isSymmetric(root) 
    print(out)
if __name__ == "__main__":
    main()
