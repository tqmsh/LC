from typing import List
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        global mx, sum, dep
        mx = 0
        sum = 0
        dep = {}
        dep[0] = 0
        def dfs(u, f):
            global mx, sum, dep
            if not u: return
            dep[u] = dep[f] + 1  
            if dep[u] == mx: sum += u.val
            elif dep[u] > mx:
                mx = dep[u]
                sum = u.val
            dfs(u.left, u)
            dfs(u.right, u)
            
        dfs(root, 0)
        return sum 

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
    values = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    root = build_BT(values)
    solution = Solution()
    print(solution.deepestLeavesSum(root))
if __name__ == "__main__":
    main()
