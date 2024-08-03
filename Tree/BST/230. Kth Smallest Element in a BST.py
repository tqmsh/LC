from typing import List 
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def _inorder(self, node, result):
        if not node:
            return
        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self._inorder(root, result)
        return result[k - 1]

    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self._inorder(root, result)
        return result[-k]

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
    root = [2,1,3]
    bst_root = solution.isValidBST(build_BT(root))
    # print("BST Structure:")
    print(bst_root)
if __name__ == "__main__":
    main()
