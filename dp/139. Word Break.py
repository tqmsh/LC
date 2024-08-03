from typing import List 
from collections import defaultdict
import math
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s); s = " " + s; dp = [0] * (n + 1)
        dp[0] = 1
        mx_l = max(len(s) for s in wordDict) 
        for i in range(1, n + 1):
            for j in range(max(0, i - mx_l), i):
                dp[i] |= (dp[j] and s[j + 1: i + 1] in wordDict)
                if dp[i]: break
        return dp[n]
                         
        
def main():
    solution = Solution()  
    s = "catsandog"; wordDict = ["cats","dog","sand","and","cat"]
    out = solution.wordBreak(s, wordDict)
    print(out) 

if __name__ == "__main__":
    main()
