from typing import List 
from collections import defaultdict
import math
class Solution: 
    def canPartition(self, nums: List[int]) -> bool:
        tot =  sum(nums)
        if tot % 2 != 0: return 0
        req = tot // 2
        dp = [0] * (req + 1) 
        dp[0] = 1
        for num in nums:
            for j in range(req, num - 1, - 1):
                dp[j] += dp[j - num]
        return dp[req] 

        
def main():
    solution = Solution()  
    nums = [1,5,11,5]
    out = solution.canPartition(nums)
    print(out) 

if __name__ == "__main__":
    main()
