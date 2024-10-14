from typing import List 
from collections import defaultdict
import math
class Solution: 
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) 
        dp[0] = 1
        
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = dp[j] + dp[j - coin] # 相当于 dp[i][j] = dp[i - 1][j] (即上一个物品计算的结果，因为目前正在算 j,
                                             # 数据还保持在上一个 i 上) + dp[i][j - coin] (j - coin 已经被处理过了，所
                                             # 以是当下 i 的数据了) 
        return dp[amount]

        
def main():
    solution = Solution()  
    amount = 5; coins = [1,2,5]
    out = solution.change(amount, coins)
    print(out) 

if __name__ == "__main__":
    main()
