from typing import List 
from collections import defaultdict
import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        # lambda 模版
        dp = defaultdict(lambda: math.inf); dp[0] = 0  
        current_farthest = 0 
        for i, num in enumerate(nums):
            current_farthest = min(len(nums) - 1, max(current_farthest, i + num))
            dp[current_farthest] = min(dp[current_farthest], dp[i] + 1)
        
        return dp[len(nums) - 1]
        
def main():
    solution = Solution()  
    nums = [2,3,0,1,4]
    out = solution.jump(nums)
    print(out) 

if __name__ == "__main__":
    main()
