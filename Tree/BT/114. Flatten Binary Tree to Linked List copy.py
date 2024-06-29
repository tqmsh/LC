from typing import List 
from typing import Optional 
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _bfs(self, root):
        queue = deque([root])
        levels = [] 
        while queue:
            depth_size = len(queue) # 一次性吧这层所有的都扩散出去
            level_now = []
            for i in range(depth_size):
                node = queue.popleft()
                level_now.append(node.val) 
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right) # 进q 前判断一般以进 q 后判断快/难写
            levels.append(level_now) 
        return levels
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        if not root: return None    
        return self._bfs(root) 
     
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
    root = build_BT([3,9,20,None,None,15,7]) 
    out = solution.levelOrder(root) 
    print(out)
if __name__ == "__main__":
    main()
