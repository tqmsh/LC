from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 子树高度 模版
    def _dfs(self, root):
        # 边枚举边计算 & 如果是利用儿子结点信息计算，先递归再计算  
        if not root: return (1, 0)

        l_is_balanced, l_height = self._dfs(root.left)
        r_is_balanced, r_height  = self._dfs(root.right)

        return (1, max(l_height, r_height) + 1) if l_is_balanced and r_is_balanced and abs(l_height - r_height) <= 1 else (0, 0)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._dfs(root)[0]
    

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
    root = build_BT([1,2,2,3,3,None,None,4,4])
    out = solution.isBalanced(root) 
    print(out)
if __name__ == "__main__":
    main()
