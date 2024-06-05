from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # f[i]: i 子树，加入val后，成啥样
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # 状态转移
        if not root: return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
            return root
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
            return root
 
def print_bst(node, level=0, label='.'):
    indent = '   ' * level
    if node is not None:
        print(f"{indent}-{label}: {node.val}")
        print_bst(node.left, level + 1, 'L')
        print_bst(node.right, level + 1, 'R')
    else:
        print(f"{indent}-{label}: None") 

def insertIntoBSTT(root: Optional[TreeNode], val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBSTT(root.left, val)
    else:
        root.right = insertIntoBSTT(root.right, val)
    return root

def buildBST(values: List[int]) -> Optional[TreeNode]:
    root = None
    for value in values:
        root = insertIntoBSTT(root, value)
    return root

def main():
    values = [4,2,7,1,3]
    val = 5
    root = buildBST(values)
    solution = Solution()
    subtree = solution.insertIntoBST(root, val)
    print_bst(subtree)
if __name__ == "__main__":
    main()
