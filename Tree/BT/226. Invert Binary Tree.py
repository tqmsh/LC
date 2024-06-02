from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # f[i]: i 子树，完全翻转后，成啥样
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 基础
        if not root: return 
        # 如果是利用儿子结点信息计算，先递归再计算   
        left = root.left
        root.left = self.invertTree(root.right) # 这里传 None 可以的
        root.right = self.invertTree(left) 
        return root

def print_bst(node, level=0, label='.'):
    indent = '   ' * level
    if node is not None:
        print(f"{indent}-{label}: {node.val}")
        print_bst(node.left, level + 1, 'L')
        print_bst(node.right, level + 1, 'R')
    else:
        print(f"{indent}-{label}: None")

# 模版 BT
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
    root = build_BT([2,3,None,1])
    out = solution.invertTree(root) 
    print_bst(out)
if __name__ == "__main__":
    main()
