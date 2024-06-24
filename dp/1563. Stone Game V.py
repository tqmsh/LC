from typing import List 
from collections import defaultdict  
from itertools import accumulate
class Solution:
    def stoneGameV(self, piles):
        dp = defaultdict(int); psa = defaultdict(int) 
        # accumulate 模版
        for i, pile in enumerate(piles): psa[i] = psa[i - 1] + pile  

        # 区间 dp 模版 
        for l in range(2, len(piles) + 1): 
            for i in range(len(piles)):  
                j = i + l - 1  
                if j >= len(piles): break 
                for k in range(i, j):
                    lSum = psa[k] - psa[i - 1]
                    rSum = psa[j] - psa[k]
                    if rSum > lSum:
                        dp[i, j] = max(dp[i, j], dp[i, k] + lSum)
                    elif rSum == lSum:
                        dp[i, j] = max(dp[i, j], max(dp[i, k], dp[k + 1, j]) + lSum)
                    else:
                        dp[i, j] = max(dp[i, j], dp[k + 1, j] + rSum) 
 
        return dp[0, len(piles) - 1]
 
def main():
    solution = Solution()  
    piles = [4]
    out = solution.stoneGameV(piles)
    print(out)

if __name__ == "__main__":
    main()
