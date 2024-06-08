# Question:
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where
# the sum of the node values in the path equals targetSum. Each path should be returned as a
# list of the node values, not node references.

# Input:
# The input is a binary tree represented as a list of node values, where each node can have
# up to two children, and an integer targetSum. This input defines the hierarchical structure
# of the tree and the target sum to be matched.

# Output:
# The output is a list of lists, where each inner list contains the node values of a root-to-leaf
# path that sums up to the targetSum, reflecting all possible paths that meet the criteria.

from typing import List 
from typing import Optional 
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:   
        ans = []
        
        def dfs(u, cur, sum):   
            
            # 进门后录，进队/门方法很多，出队/门就一种，好写; 这里，进门 = u.l/r, 出门 = u; 处理 u

            if not u: return 

            if not u.left and not u.right and sum == targetSum: 
                ans.append(cur)
                return 
            
            if u and u.left: dfs(u.left, cur + [u.left.val], sum + u.left.val)
            if u and u.right: dfs(u.right, cur + [u.right.val], sum + u.right.val)   
            
        if root == None: return []
        
        dfs(root, [root.val], root.val) # 这个坑 (dfs 进门) 用 root.l/r 填，维持 root, 方便录；这里基用的是有一个 rt 的情况

        # bfs
        if root == None: return [] # 🟥 edge case 防最上
        ans = []
        q = deque([(root, [root.val], root.val)])  
        def bfs(): 
            while q:
                u, cur, sum = q.popleft()
                if not u: continue
                if not u.left and not u.right and sum == targetSum: 
                    ans.append(cur)
                    continue 
                if u and u.left: q.append((u.left, cur + [u.left.val], sum + u.left.val))
                if u and u.right: q.append((u.right, cur + [u.right.val], sum + u.right.val))    

        bfs()
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

def main():
    solution = Solution()
    root = [1,2]; targetSum = 3
    root = build_BT(root)
    out = solution.pathSum(root, targetSum) 
    print(out)
if __name__ == "__main__":
    main()
