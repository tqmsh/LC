# Question:
# Given the root of a binary tree, return the length of the longest ZigZag path, where a ZigZag path
# starts at any node and alternates between moving right and left child nodes.

# Input:
# The input is the root of a binary tree represented as a list of node values, where each node can
# have up to two children. This input defines the hierarchical structure of the tree.

# Output:
# The output is an integer representing the length of the longest ZigZag path in the tree,
# measured as the number of nodes visited minus one.

from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        global ans
        ans = 0
        # f[i][x][y]: i 子树, 进点时走的是 (x/ y), 最长路径为 x/ y 的数值

        # ans = max(所有 i 子树 的 x/ y 的数值)
        def dfs(u, l, r):
            global ans
            ans = max(ans, l, r)

            # 状态转移
            if u.left: dfs(u.left, r + 1, 0)
            if u.right: dfs(u.right, 0, l + 1) 

        # 基
        dfs(root, 0, 0) 
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
    root = build_BT([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
    # root = build_BT([1, None, 1, 1, None])
    out = solution.longestZigZag(root) 
    print(out)

if __name__ == "__main__":
    main()
