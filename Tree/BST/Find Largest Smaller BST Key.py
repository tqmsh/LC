from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    def findLargestSmallerKey(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = 0
        while root:
            if root.val < val:
                ans = root.val
                root = root.right
            else:
                root = root.left
        return ans
 
def print_bst(node, level=0, label='.'):
    indent = '   ' * level
    if node is not None:
        print(f"{indent}-{label}: {node.val}")
        print_bst(node.left, level + 1, 'L')
        print_bst(node.right, level + 1, 'R')
    else:
        print(f"{indent}-{label}: None") 

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
    values = [9, 2, 7, 1, 3]
    val = 8
    root = buildBST(values)
    solution = Solution()
    subtree = solution.findLargestSmallerKey(root, val)
    print(subtree)
if __name__ == "__main__":
    main()
