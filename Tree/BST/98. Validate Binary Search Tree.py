from typing import List 
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # dp[u]: u 子树是否是BST
    # mn / mx: [rt, u)，如果按照 BST 规则，能够推出的最值
    # dp[u] = mn >= root.val & root.val >= mx & π dp[v], 优化至直传
    def _dfs(self, u, step_mn, step_mx):
        if not u: return 1
        if not (step_mn < u.val < step_mx): return 0
        return self._dfs(u.left, step_mn, u.val) and self._dfs(u.right, u.val, step_mx)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._dfs(root, -float('inf'), float('inf')) # 对于 rt，按照 BST 规则, 没有限制
    

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
    root = [2,1,3]
    bst_root = solution.isValidBST(build_BT(root))
    # print("BST Structure:")
    print(bst_root)
if __name__ == "__main__":
    main()
