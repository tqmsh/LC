from typing import List 
from collections import defaultdict  
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s); dp = defaultdict(lambda: float('inf')) 
        for i in range(n): dp[i, i] = 1
        
        # dp[i][j]: [i, j]，最少花多少笔？考虑到 i - 1 & j + 1 一笔画的情况下
        for l in range(2, n + 1):
            for i in range(n):
                j = i + l - 1
                if j >= n: break 
                if s[i] == s[j]:
                    dp[i, j] = dp[i, j - 1]
                else:
                    for k in range(i, j): dp[i, j] = min(dp[i, j], dp[i, k] + dp[k + 1, j])
        return dp[0, n - 1] 
 
def main():
    solution = Solution()  
    s = "acacdccb"
    out = solution.strangePrinter(s)
    print(out)

if __name__ == "__main__":
    main()
