from typing import List 
from collections import defaultdict
import math
class Solution:
    def racecar(self, target: int) -> int: 
        # dp 初始化 模版
        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            dp[i] = float('inf')
            j = 0; pos = 0
            while j < i:
                k = 0; neg = 0
                while k < j:
                    dp[i] = min(dp[i], pos + neg + 2 + dp[i - (j - k)]) 
                    neg += 1; k = (1 << neg) - 1
                pos += 1; j = (1 << pos) - 1
            dp[i] = min(dp[i], pos + (j != i) + dp[j - i])
        return dp[target]
    
def main():
    solution = Solution()  
    target = 3
    out = solution.racecar(target)
    print(out) 

if __name__ == "__main__":
    main()
