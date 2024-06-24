from typing import List 
from collections import defaultdict
import math
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:   
        dp = defaultdict(int)
        sum = 0 
        for i in range(len(piles) - 1, -1, -1): 
            sum += piles[i] # [i, len)
            for j in range(1, (len(piles) + 1)/2 + 1): # j > n - i / 2 就答案一样了
                                                       #, j 枚举至 n / 2 + 1 即可
                # 基 
                if i + 2*j > len(piles):
                    dp[i, j] = sum
                else:
                    for k in range(1, 2 * j + 1):
                        dp[i, j] = max(dp[i, j], sum - dp[i + k, max(j, k)])
        return dp[0, 1] 
def main():
    solution = Solution()  
    piles = [1]
    out = solution.stoneGameII(piles)
    print(out) 

if __name__ == "__main__":
    main()
