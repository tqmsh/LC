from typing import List 
from collections import defaultdict
import math
class Solution:
    # 第一 >= 模版
    def _build_larger(self, arr, larger):
        stk = [] 
        # 从小到大，保证绿色位于黑色右边
        for i in range(len(arr)):
            # 绿色覆盖黑色, 对于黑色的来说，绿色的值是第一 >= 黑色的值 
            while stk and arr[stk[-1]] <= arr[i]:
                larger[stk.pop()] = i
            stk.append(i) 
    # 第一 < 模版
    def _build_smaller(self, arr, smaller):
        stk = [] 
        # 从小到大，保证绿色位于黑色右边
        for i in range(len(arr)):
            # 绿色覆盖黑色, 对于黑色的来说，绿色的值是第一 >= 黑色的值 
            while stk and arr[stk[-1]] > arr[i]:
                smaller[stk.pop()] = i
            stk.append(i) 
 
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        larger = defaultdict(lambda: -1); self._build_larger(nums, larger)
        smaller = defaultdict(lambda: -1); self._build_smaller(nums, smaller)    
        dp = defaultdict(lambda: math.inf); dp[0] = 0   
        for i in range(len(nums)):
            if larger[i] != -1: 
                dp[larger[i]] = min(dp[larger[i]], dp[i] + costs[larger[i]])   
            if smaller[i] != -1:  
                dp[smaller[i]] = min(dp[smaller[i]], dp[i] + costs[smaller[i]])     
        # return dp[len(nums) - 1]
        
        # 优化，边枚举边计算
        stk_inc = []; stk_dec = []
        for i, num in enumerate(nums):
            while stk_inc and nums[stk_inc[-1]] <= nums[i]: # 第一 >=
                dp[i] = min(dp[i], dp[stk_inc.pop()] + costs[i])  
            while stk_dec and nums[stk_dec[-1]] > nums[i]: # 拿 第一 < 
                dp[i] = min(dp[i], dp[stk_inc.pop()] + costs[i])  
            stk_inc.append(i)
            stk_dec.append(i)
        return dp[len(nums) - 1]

def main():
    solution = Solution()  
    nums = [0,1,2]; costs = [1,1,1]
    out = solution.minCost(nums, costs)
    print(out) 

if __name__ == "__main__":
    main()
