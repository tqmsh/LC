from typing import List 
from collections import defaultdict
import math
from functools import lru_cache

class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)
        dp = [[0] * (n + 1) for _ in range(n)]
        dp[0][1] = 1
        for i in range(n):
            for k in range(i):
                d = stones[i] - stones[k]
                if d > i: continue # 可能性剪枝；idx 0 -> idx 1: d_mx = 1; idx k - 1 -> idx k: d_mx = k
                for j in range(d - 1, d + 2): dp[i][j] |= (dp[k][d] if d >= 0 else 0)
        return any(dp[n - 1])
    
    @lru_cache(None)
    def _dp(self, i, k, stones, s): 
        return i == stones[-1] or any(
            x and x + i in s and self.dp(i + x, x)
            for x in range(k - 1, k + 2)
        )
    def canCross(self, stones: list[int]) -> bool:
        s = set(stones) 
        return self.dp(stones[0], 0)

    
def main():
    solution = Solution()  
    stones = [0,1,3,5,6,8,12,17]
    out = solution.canCross(stones)
    print(out) 

if __name__ == "__main__":
    main()
