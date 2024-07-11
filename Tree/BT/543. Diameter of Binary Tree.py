from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    # 树直径 模版
    # dp[i]: i 子树，至叶子，最长路径
    # dp[i] = max(dp[l], dp[r]) + 
    # dp[null] = 0
    # ans = max(dp[i])
    def _dfs(self, node, ans):
        if not node: return 0
        l = self._dfs(node.left, ans)
        r = self._dfs(node.right, ans)
        ans[0] = max(ans[0], l + r)
        return max(l, r) + 1 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self._dfs(root, ans)
        return ans[0]
    
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
    root = build_BT([1,2,3,4,5])
    out = solution.diameterOfBinaryTree(root) 
    print(out)
if __name__ == "__main__":
    main()
