from typing import List
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # bst 列排序 模版
        def makeA(root, a):
            if not root: return
            makeA(root.left, a)
            # 如果是利用儿子结点信息计算，先递归再计算  
            a += [root.val]
            makeA(root.right, a)
        a = []
        makeA(root, a)
        
        # 双指针
        i, j = 0, len(a) - 1  
        ans = 0
        while (i < j): 
            ans |= (k == a[i] + a[j])  
            # 枚举优化，删除不必要的枚举；将高的移动没有意义，不可能更优，只移低的
            if (a[i] + a[j] > k): j -= 1
            else: i += 1
             
        return ans  
    

def insertIntoBST(root: Optional[TreeNode], val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
 
def buildBST(values: List[int]) -> Optional[TreeNode]:
    root = None
    for value in values:
        root = insertIntoBST(root, value)
    return root

def main():
    values = [5,3,6,2,4,7]
    k = 9
    root = buildBST(values)
    solution = Solution()
    print(solution.findTarget(root, k))
if __name__ == "__main__":
    main()
