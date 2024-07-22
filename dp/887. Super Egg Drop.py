from typing import List 
from collections import defaultdict
import math
class Solution:
    def _T(self, dp, i, j, x): # f(x) 单调递增 
        return max(dp[i][j - x], dp[i - 1][x - 1]) <= max(dp[i][j - (x + 1)], dp[i - 1][(x + 1) - 1])
    
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(k + 1)] 
        # 初始化 
        for j in range(n + 1): dp[1][j] = j # k >= 1

        for i in range(2, k + 1):
            min_idx = 0 
            for j in range(1, n + 1): # n >= 1
                if min_idx < j and not self._T(dp, i, j, min_idx): min_idx += 1 
                dp[i][j] = 1 + max(dp[i - 1][min_idx - 1], dp[i][j - min_idx])

        return dp[k][n] 

        
def main():
    solution = Solution()  
    k = 3; n = 14
    out = solution.superEggDrop(k, n)
    print(out) 

if __name__ == "__main__":
    main()
