from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # Base Case
        if not root: return ""

        # Inductive case
        dp_l_s = self.tree2str(root.left)
        dp_r_s = self.tree2str(root.right)

        # Case work, piece together dp_rt
        if root.left and root.right: return f"{root.val}({dp_l_s})({dp_r_s})"
        elif root.left: return f"{root.val}({dp_l_s})" 
        elif root.right: return f"{root.val}()({dp_r_s})"
        else: return (str(root.val))
def print_bst(node, level=0, label='.'):
    indent = '   ' * level
    if node is not None:
        print(f"{indent}-{label}: {node.val}")
        print_bst(node.left, level + 1, 'L')
        print_bst(node.right, level + 1, 'R')
    else:
        print(f"{indent}-{label}: None")
 
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
    root1 = build_BT([1,2,3,4]) 
    out = solution.tree2str(root1)  
    print(out)

if __name__ == "__main__":
    main()
