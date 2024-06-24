from typing import List 
from collections import deque, defaultdict

class Solution: 
    def _build_larger(self, arr, larger):
        stk = []
        # 从小到大，确保绿色数值 >= 黑色数值
        for i, x in sorted(enumerate(arr), key=lambda x: (x[1], x[0])): 
            # 绿色覆盖黑色, 对于黑色的来说，绿色的指数是第一 >= 黑色的指数的，即是右边最靠近自己的绿色
            while stk and stk[-1] < i:
                larger[stk.pop()] = i
            stk.append(i)
    def _build_smaller(self, arr, smaller):
        stk = [] 
        for i, x in sorted(enumerate(arr), key=lambda x: (-x[1], x[0])):  
            while stk and stk[-1] < i:
                smaller[stk.pop()] = i
            stk.append(i)
    def oddEvenJumps(self, arr: List[int]) -> int:
        # [i, ∞)大/小至近 模版
        larger = defaultdict(lambda: -1); self._build_larger(arr, larger)
        smaller = defaultdict(lambda: -1); self._build_smaller(arr, smaller)  
        even = defaultdict(int); odd = defaultdict(int); even[len(arr) - 1] = 1; odd[len(arr) - 1] = 1 
        # reversed 模版
        for i in reversed(range(len(arr) - 1)):
            if smaller[i] != -1: odd[i] = even[smaller[i]]
            if larger[i] != -1: even[i] = odd[larger[i]]
        ans = 0
        for i in range(len(arr)): ans += even[i]
        return ans
def main(): 
    solution = Solution()  
    out = solution.oddEvenJumps([10,13,12,14,15]) 
    print(out) 

if __name__ == "__main__":
    main()