from typing import List 
from collections import defaultdict
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        dp = defaultdict(int) 
        dp[(0, 0)] = 0   
        dp[(0, 1)] = -prices[0]   
        dp[(1, 0)] = max(dp[(0, 0)], dp[(0, 1)] + prices[1])  # 想要钱，随便卖
        dp[(1, 1)] = max(dp[(0, 1)], -prices[1])  # 想持有股，就买, 不能用昨天赚的钱继续

        for i in range(2, len(prices)):
            dp[(i, 0)] = max(dp[(i - 1, 0)], dp[(i - 1, 1)] + prices[i])
            dp[(i, 1)] = max(dp[(i - 1, 1)], dp[(i - 2, 0)] - prices[i]) 
        
        return dp[(len(prices) - 1, 0)]
 
def main():
    solution = Solution()  
    nums = [1,2,3,0,2]
    out = solution.maxProfit(nums)
    print(out) 

if __name__ == "__main__":
    main()
