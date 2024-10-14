from collections import deque
from typing import Optional, Deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:   
        ans = -float('inf')
        q: Deque[tuple[TreeNode, int]] = deque([(root, 1)])
        while q:
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                u, x = q.popleft()
                if u.left: q.append((u.left, 2 * x))
                if u.right: q.append((u.right, 2 * x + 1))
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
print(Solution().widthOfBinaryTree(build_BT([1,3,2,5,None,None,9,6,None,7])))