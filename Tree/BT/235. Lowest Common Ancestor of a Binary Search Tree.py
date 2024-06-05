from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # stk 模版
        ans = []; stk = []; tmp = root #🟥ans = stk = [] 不可，因为地址一致
        while stk or tmp:

            # 模拟移至左边最深
            while tmp:
                stk += [tmp] #后进先出
                tmp = tmp.left
            
            # 模拟左边到底了，往上倒滑至第一个有右岔路的地方 
            tmp = stk.pop()  
            ans += [tmp.val] 
            tmp = tmp.right # 尝试去右边岔路，如果存在的话，下次就去 while tmp 移至左边最深了
        
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
    root = build_BT([1,None,2,3])
    out = solution.inorderTraversal(root) 
    print(out)
if __name__ == "__main__":
    main()
