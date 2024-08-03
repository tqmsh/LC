from typing import List 
from collections import deque

class Solution:
    def countWays(self, n: int) -> int:
        # dp[i][j]: 至 i, 目前时间是基/欧 (j), 方案数
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0] = 0; dp[0][1] = 1
        for i in range(1, n + 1): 
            if i - 2 >= 0: dp[i][0] += dp[i - 2][1] 
            if i - 3 >= 0: dp[i][0] += dp[i - 3][1]
            dp[i][1] += dp[i - 1][0] 
            if i - 2 >= 0: dp[i][1] += dp[i - 2][0]  
        return dp[n][0] + dp[n][1]
    
def main(): 
    solution = Solution() 
    n = 101
    out = solution.countWays(n) 
    print(out) 

if __name__ == "__main__":
    main()