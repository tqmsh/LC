from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int: 
        # 初始化
        if not root: return 0
        # 状态转移 
        if low <= root.val <= high: return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) 
        elif root.val < low:
            # x < low, L < x => L < low，跳过
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
             return self.rangeSumBST(root.left, low, high)
def insertIntoBST(root: Optional[TreeNode], val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
 
def buildBST(values: List[int]) -> Optional[TreeNode]:
    root = None
    for value in values:
        root = insertIntoBST(root, value)
    return root
 
def main():
    root = [10,5,15,3,7,13,18,1,6]
    low = 6; high = 10
    root = buildBST(root)
    solution = Solution()
    subtree = solution.rangeSumBST(root, low, high)
    print(subtree)
if __name__ == "__main__":
    main()
