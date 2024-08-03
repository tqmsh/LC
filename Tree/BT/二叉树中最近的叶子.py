from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def min_iterations_to_pass_info(self, root: Optional[TreeNode]):
        q = [(root, 0)]
        while q:
            now, path = q.pop(0)
            if now is None: return path
            q.extend([(now.left, path + 1), (now.right, path + 1)]) 
            
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
    root = build_BT([1,3,2,4])
    k = 1
    out = solution.min_iterations_to_pass_info(root) 
    print(out)
if __name__ == "__main__":
    main()
