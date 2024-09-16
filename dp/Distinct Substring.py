from typing import List 
from collections import defaultdict
import math
class Solution:
    def numDistinct(self, s: str, t: str) -> int: # diff from f[R] = f[L] + idx, coz its asking for
                                                  # of distinct substr = t, not how many counts in
                                                  # all substr
        n = len(s); s = " " + s
        m = len(t); t = " " + t
        # dp 初始化  
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1): dp[i][0] = 1

        # 状态转移
        for i in range(1, n + 1):
            for j in range(1, m + 1): 
                dp[i][j] = dp[i - 1][j]
                if s[i] == t[j]: dp[i][j] += dp[i - 1][j - 1] # 🟥 i & j mixups
        return dp[n][m]

        
def main():
    solution = Solution()  
    s = "babgbag"; t = "bag"
    out = solution.numDistinct(s, t)
    print(out) 

if __name__ == "__main__":
    main()
