from typing import List 
from collections import defaultdict
import math
class Solution: 
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) 
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        
        return -1 if dp[amount] == float('inf') else dp[amount]

        
def main():
    solution = Solution()  
    amount = 5; coins = [1,2,5]
    out = solution.coinChange(amount, coins)
    print(out) 

if __name__ == "__main__":
    main()
