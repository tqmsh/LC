from typing import List 
from collections import defaultdict  
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 处理边界
        nums = [1] + nums + [1] # wlog len >= 3
        dp = [[0] * len(nums) for _ in range(len(nums))]  
        
        for l in range(3, len(nums) + 1): 
            for i in range(len(nums)):  
                j = i + l - 1  
                if j >= len(nums): break 
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[k] * nums[i] * nums[j]) 
 
        return dp[0][len(nums) - 1]

def main():
    solution = Solution()  
    nums = [1,5]
    out = solution.maxCoins(nums)
    print(out)


if __name__ == "__main__":
    main()
