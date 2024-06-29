from typing import Optional, Generator

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
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
  

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.iter = self._inorder(root) 
        self.ptr = next(self.iter, None) # 把咱的指针放在root及后第一位

    def __init__(self, root: Optional[TreeNode]): 
        self.iter = self._inorder(root) 
        self.ptr = next(self.iter, None)
    
    def _inorder(self, node: Optional[TreeNode]) -> Generator[int, None, None]:
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)
 
    def next(self) -> int:   
        res = self.ptr # 把指针状态给出 
        self.ptr = next(self.iter, None) # 右移指针
        return res

    def hasNext(self) -> bool: 
        return self.ptr is not None
    
# Construct the BST
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

# Initialize the iterator
iterator = BSTIterator(root)

# Iterate over the BST
print(iterator.next())    # return 3
print(iterator.next())    # return 7
print(iterator.hasNext()) # return True
print(iterator.next())    # return 9
print(iterator.hasNext()) # return True
print(iterator.next())    # return 15
print(iterator.hasNext()) # return True
print(iterator.next())    # return 20
print(iterator.hasNext()) # return False
