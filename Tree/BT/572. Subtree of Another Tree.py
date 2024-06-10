from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
   
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return 0
        if self.isSameTree(root, subRoot): return 1
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)  

    # isSameTree 模版
    def isSameTree(self, p, q):
        if not p or not q:
            if p == q: return 1
            return 0
        if p.val != q.val: 
            return 0
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
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
    root = build_BT([3,4,5,1,2])
    subRoot = build_BT([4,1,2])
    out = solution.isSubtree(root, ) 
    print(out)
if __name__ == "__main__":
    main()
