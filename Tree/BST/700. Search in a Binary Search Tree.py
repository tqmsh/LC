from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.dfs(root, val)
    
    def dfs(self, node: TreeNode, val) :
        if not node: return None
        
        if val == node.val: return node
        
        if val > node.val: return self.dfs(node.right, val)
            
        if val < node.val: return self.dfs(node.left, val)

# BST 模版
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
    values = [4, 2, 7, 1, 3]
    val = 7
    root = buildBST(values)
    solution = Solution()
    subtree = solution.searchBST(root, val)
    print_bst(subtree)
if __name__ == "__main__":
    main()
