from typing import List 
from collections import defaultdict
import math
class Solution:
    def expectMaximum(self, nums):
        n = len(nums); nums = [0] + nums + [0]
        dp = [0] * (n + 1); stk = [];  
        for i in range(1, n + 1):
            while stk and nums[stk[-1]] <= nums[i]: stk.pop()
                # 以 i 结尾的子序列是由 [0, i) 结尾的子序列经过 i 形成的
            if stk: dp[i] = (i - stk[-1]) * nums[i]              +   dp[stk[-1]]
                    #    （stk[-1]， i]的子序列经过 i 后最大值产生的变化      而 [0, stk[-1]] 的子序列经过 i 后没变
            else: dp[i] = i * nums[i]  
            stk.append(i)
        return sum(dp) / (n * (n + 1) // 2)

def main():
    solution = Solution()  
    nums =  [1, 2, 3]
    out = solution.expectMaximum(nums)
    print(out) 

if __name__ == "__main__":
    main()
