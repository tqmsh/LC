# Question:
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Input:
# The input is a binary tree represented as a list of node values, where each node can have up to two children. This input defines the hierarchical structure of the tree.

# Output:
# The output is a list of integers representing the values of the nodes visible from the right side of the binary tree, ordered from top to bottom.
from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
        a = []; ans = []
        # dep 模版
        def dfs(u, h):
            if not u: return        
            if len(a) == h: a.append([]) #🟥如果不想 global a 的话就 append
            a[h].append(u)
            dfs(u.right, h + 1)
            dfs(u.left, h + 1) 
        dfs(root, 0)
        print(a)
        for x in a:
            ans += [x[-1].val]
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
    root = build_BT([1,2,3,None,5,None,4])
    # root = build_BT([1, None, 1, 1, None])
    out = solution.rightSideView(root) 
    print(out)

if __name__ == "__main__":
    main()
