from typing import List, Optional
from collections import defaultdict
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
    # mn/mx[i]: i 子树，如为 bst, 最小/大值; 如不为 bst, 则 -inf, inf
    # if mx[i.l] < u.val < mn[i.r]: mn/mx[i] = min(i.val, mn[i.l])/ max(i.val, mx[i.r]) 
    # else: mn/mx[!bst] = -inf, inf 

    # sz[i]: i 子树，如为 bst, 最小/大值 
    
    # mn/mx[None] = inf, -inf
    def _dfs(self, u: TreeNode, ans):
        if not u: return (float('inf'), -float('inf'), 0)
        mn_l, mx_l, sz_l = self._dfs(u.left, ans)
        mn_r, mx_r, sz_r = self._dfs(u.right, ans)

        # 如果是利用儿子结点信息计算，先递归再计算  
        if mx_l < u.val < mn_r:
            ans[0] = max(ans[0], sz_l + 1 + sz_r) 
            mn_u = min(u.val, mn_l); mx_u = max(u.val, mx_r); sz_u = sz_l + sz_r + 1
            return (mn_u, mx_u, sz_u)

        return (-float('inf'), float('inf'), 0)  
    


    # 写法二
    def _dfs2(self, u: TreeNode, ans, sz, mn, mx):
        # 初始化
        if not u:
            sz[u] = 0; mn[u] = float('inf'); mx[u] = -float('inf')
            return
        
        self._dfs2(u.left, ans, sz, mn, mx)
        self._dfs2(u.right, ans, sz, mn, mx)

        if mx[u.left] < u.val < mn[u.right]:
            ans[0] = max(ans[0], sz[u.left] + 1 + sz[u.right]) 
            mn[u] = min(u.val, mn[u.left]); mx[u] = max(u.val, mx[u.right]); sz[u] = sz[u.left] + sz[u.right] + 1
        else: mn[u] = -float('inf'); mx[u] = float('inf'); sz[u] = 0
    
    def largestBSTSubtree(self, u: TreeNode):
        ans = [0]
        sz = defaultdict(int); mn = defaultdict(int); mx = defaultdict(int)
        # self._dfs(u, ans)
        self._dfs2(u, ans, sz, mn, mx)
        return ans[0]

    



        

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
    root = [4,2,7,2,3,5,None,2,None,None,None,None,None,1]
    bst_root = solution.largestBSTSubtree(build_BT(root))
    print(bst_root)
if __name__ == "__main__":
    main()
