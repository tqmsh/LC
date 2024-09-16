from typing import List 
from collections import defaultdict
import math
class Solution:
    def eatTheBeans(self, w, r):
        n = (w + r) * 2
        dp = [[[0.0] * (r + 1) for _ in range(w + 1)] for _ in range(n + 1)]
        dp[0][w][r] = 1
        for i in range(1, n + 1):
            for j in range(w + 1):
                for k in range(r + 1):
                    if i % 2 == 1: 
                        a = (dp[i - 1][j + 1][k] if j + 1 <= w else 0) 
                        b = ((j + 1) / ((j + 1) + k) if j + 1 + k != 0 else 0)
                        c = dp[i - 1][j][k]
                        d =  (k / (j + k) if j + k != 0 else 0) 
                        dp[i][j][k] = a * b + c * d
                    else: 
                        a = (dp[i - 1][j + 1][k] if j + 1 <= w else 0)
                        b = ((j + 1) / (j + 1 + k) if j + 1 + k != 0 else 0)
                        c = (dp[i - 1][j][k + 1] if k + 1 <= r else 0)
                        d = ((k + 1) / (j + k + 1) if j + k + 1 != 0 else 0) 
                        dp[i][j][k] = a * b + c * d
        ans = 0.0
        for i in range(n + 1): ans += dp[i][1][0]
        return ans
    
def main():
    solution = Solution()  
    w = 3; r = 1
    out = solution.eatTheBeans(w, r)
    print(out) 


if __name__ == "__main__":
    main()
