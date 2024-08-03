from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pre_to_in(self, pre: List[int])-> List[int]:
        # better than O(nlogn) for sorting a preorder list LOL
        stk = []; ans = []
        for x in pre:
            while stk and x > stk[-1]: ans.append(stk.pop())
            stk.append(x)
        while stk: ans.append(stk.pop())
        return ans
    
def main():
    solution = Solution() 
    out = solution.pre_to_in([-1]) 
    print(out)

if __name__ == "__main__":
    main()


