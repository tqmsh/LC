from typing import List 
from typing import Optional 
from collections import defaultdict
class Treeu:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def pathSum(self, root: Optional[Treeu], targetSum: int) -> int: 
        # defaultdict 模版
        psa = defaultdict(int)
        psa[0] = 1
        def dfs(u, sum):
            ans = 0
            if u == None: return ans
            ans += psa[sum + u.val - targetSum]
            psa[sum + u.val] += 1
            if u.left: ans += dfs(u.left, sum + u.val)
            if u.right: ans += dfs(u.right, sum + u.val)
            psa[sum + u.val] -= 1
            return ans
        return dfs(root, 0)
        
 
        
def build_BT(arr):
    if not arr:
        return None
    root = Treeu(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        current = queue.pop(0)
        if arr[i] is not None:
            current.left = Treeu(arr[i])
            queue.append(current.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            current.right = Treeu(arr[i])
            queue.append(current.right)
        i += 1
    return root
def print_bst(u, level=0, label='.'):
    indent = '   ' * level
    if u is not None:
        print(f"{indent}-{label}: {u.val}")
        print_bst(u.left, level + 1, 'L')
        print_bst(u.right, level + 1, 'R')
    else:
        print(f"{indent}-{label}: None")
def main():
    solution = Solution()
    root = build_BT([0, 1, 1])  
    targetSum = 1
    out = solution.pathSum(root, targetSum) 
    print(out)
if __name__ == "__main__":
    main()
