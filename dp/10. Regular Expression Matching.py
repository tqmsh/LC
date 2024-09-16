from typing import List 
from collections import defaultdict
import math
class Solution:
    def _check(self, i, j, s, p): return s[i] == p[j] or p[j] == '.' 
        
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s); s = " " + s
        m = len(p); p = " " + p

        # dp 初始化 模版
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1 
        for j in range(2, m + 1): dp[0][j] = dp[0][j - 2] if p[j] == '*' else 0

        # 状态转移
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j] != '*': dp[i][j] = dp[i - 1][j - 1] if self._check(i, j, s, p) else 0
                else:
                    dp[i][j] = dp[i][j - 2]
                    if self._check(i, j - 1, s, p): dp[i][j] |= dp[i - 1][j]
        return dp[n][m]


def main():
    solution = Solution()  
    s = "aa"; p = "c*a*"
    out = solution.isMatch(s, p)
    print(out) 

if __name__ == "__main__":
    main()
