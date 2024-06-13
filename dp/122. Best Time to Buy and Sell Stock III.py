from typing import List 
from collections import defaultdict
import math
class Solution: 
    def maxProfit(self, prices: List[int]) -> int: 
        dp = defaultdict(int)         
        # f[i][j][k]: i 天，持有股票/现金，卖次数: 最大收益
        dp[(0, 0)] = -math.inf
        dp[(0, 1)] = -math.inf
        dp[(0, 2)] = -math.inf 
        # 今天持有现金 => 昨天已经持有现金 OR 昨天持有股票, 今天卖了
        # 今天持有股票 => 昨天已经持有股票 OR 昨天持有现金, 今天买了 

        for price in prices: 
            dp[1, 1] = max(dp[1, 1], dp[0, 1] + price)
            dp[0, 1] = max(dp[0, 1],  dp[1, 0] - price)
            
            dp[1, 2] = max(dp[1, 2], dp[0, 2] + price) 
            dp[0, 2] = max(dp[0, 2], dp[1, 1] - price) 
        return dp[1, 2]

    # 贪心 & 前缀后缀
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]; max_price = prices[-1]; max_profit_left = [0] * len(prices); max_profit_right = [0] * len(prices) 
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit_left[i] = max_profit_left[i - 1] 
            if prices[i] < min_price: min_price = prices[i] 
            else: 
                max_profit_left[i] = max(max_profit_left[i], prices[i] - min_price)  

        for i in range(len(prices)-2, -1, -1):
            max_profit_right[i] = max_profit_right[i + 1] 
            if prices[i] > max_price: max_price = prices[i] 
            else:
                max_profit_right[i] = max(max_profit_right[i], max_price - prices[i])  
            max_profit = max(max_profit, max_profit_right[i] + max_profit_left[i]) 
        return max_profit 
def main():
    solution = Solution()  
    nums = [7,6,4,3,1]
    out = solution.maxProfit(nums)
    print(out) 

if __name__ == "__main__":
    main()
