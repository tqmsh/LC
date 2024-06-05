
# Question:
# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

# Input:
# The input is a binary tree represented as a list of node values, where each node can have
# up to two children. This input represents the hierarchical structure of a tree, crucial for
# identifying leaf nodes and their common ancestors.

# Output:
# The output is the value of the lowest common ancestor of the deepest leaves, reflecting the
# node at the greatest depth where all deepest leaves converge.

from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    # LCA 模版
    def lca(self, root, p, q):
        if root in (None, p, q): return root
        l = self.lca(root.left, p, q)
        r = self.lca(root.right, p, q)
        return root if l and r else l or r 
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        global lowestNodes, deepestDepth
        lowestNodes = []
        deepestDepth = 0
        def dfs(node, depth): 
            global lowestNodes, deepestDepth
            if not node: return 
            if depth == deepestDepth:
                lowestNodes += [node]
            elif depth > deepestDepth:
                deepestDepth = depth
                lowestNodes = [node]
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        p, q = lowestNodes[0], lowestNodes[-1]
        return self.lca(root, p, q)
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
    root = build_BT([3,5,1,6,2,0,8,None,None,7,4])
    out = solution.lcaDeepestLeaves(root) 
    print_bst(out)
if __name__ == "__main__":
    main()
