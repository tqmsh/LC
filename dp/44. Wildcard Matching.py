from typing import List 
from collections import defaultdict
import math
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = " " + s
        p = " " + p

        # dp 初始化 模版
        dp = [[0] * (len(p)) for _ in range(len(s))]
        dp[0][0] = 1

        # 初始化
        for j in range(1, len(p)):
            if p[j] == '*':
                dp[0][j] = dp[0][j - 1]

        # 状态转移
        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    dp[i][j] = dp[i - 1][j] | dp[i][j - 1]

        return dp[len(s) - 1][len(p) - 1]

        
def main():
    solution = Solution()  
    s = "cb"; p = "?a"
    out = solution.isMatch(s, p)
    print(out) 

if __name__ == "__main__":
    main()
