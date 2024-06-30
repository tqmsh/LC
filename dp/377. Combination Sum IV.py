
from typing import List 
from collections import deque

class Solution: 
    def combinationSum4(self, nums: List[int], target: int) -> int: 
        dp = [0] * (target + 10)

        # 基
        dp[0] = 1

        # 状态转移 
        for i in range(target + 1):
            for x in nums: 
                if i - x >= 0:
                    dp[i] += dp[i - x]

        # 记忆化 模版
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            
            if i == 0: return 1

            val = 0 
            for x in nums: 
                if i - x >= 0:
                    val += dp(i - x)
            
            memo[i] = val
            return val
        
        return dp(target)
def main(): 
    solution = Solution()  
    nums = [1,2,3]; target = 4
    out = solution.combinationSum4(nums, target) 
    print(out) 

if __name__ == "__main__":
    main()