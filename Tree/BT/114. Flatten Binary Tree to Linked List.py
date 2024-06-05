from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:  
        # 基
        if not root: return None 

        # 如果是利用儿子结点信息计算，先递归再计算   
        l = self.flatten(root.left)
        r = self.flatten(root.right) 

        root.left = None
        root.right = l

        # 拿 l 尾部地址
        tmp = l   
        while tmp and tmp.right: # 把 tmp 移至 l 尾部
            tmp = tmp.right
        
        # 拿到了
        if tmp: tmp.right = r 

        # 没拿到
        else: root.right = r
        
        return root 

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
    root = build_BT([1,2,5,3,4,None,6])
    out = solution.flatten(root) 
    print_bst(out)
if __name__ == "__main__":
    main()
