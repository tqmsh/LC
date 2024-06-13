from typing import List 
from collections import defaultdict
import math
class Solution: 
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = defaultdict(int)       
        for j in range(0, k + 1): dp[(0, j)] = -math.inf  
        for price in prices: 
            for j in range(1, k + 1):
                dp[1, j] = max(dp[1, j], dp[0, j] + price) 
                dp[0, j] = max(dp[0, j],  dp[1, j - 1] - price) 
        return dp[1, k] 
def main():
    solution = Solution()  
    out = solution.maxProfit(2, [3,2,6,5,0,3])
    print(out) 

if __name__ == "__main__":
    main()
