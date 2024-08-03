from typing import List 
from collections import defaultdict
import math
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        if n == 0: return 0
        dp1, dp2 = 0, 1
        if s[0] == "*": dp1 = 9
        elif s[0] != '0': dp1 = 1
        for i in range(1, n):
            dp = 0
            if s[i] == "*":
                dp = dp1 * 9 % MOD
                if s[i - 1] == "2": dp += (dp2 if i >= 2 else 1) * (26 - 21 + 1) % MOD
                if s[i - 1] == "1": dp += (dp2 if i >= 2 else 1) * (19 - 11 + 1) % MOD
                if s[i - 1] == "*": dp += (dp2 if i >= 2 else 1) * (26 - 11) % MOD
            else:
                if s[i] != '0': dp = dp1 
                if "10" <= s[i - 1] + s[i] <= "26": dp += (dp2 if i >= 2 else 1) % MOD
                if s[i - 1] == "*":
                    for x in ["1", "2"]:
                        if "10" <= x + s[i] <= "26": dp += (dp2 if i >= 2 else 1) % MOD
            dp %= MOD
            dp2, dp1 = dp1, dp
        return dp1
    def preprocess(self, s: str) -> int: 
        mp = defaultdict(int); M = 10 ** 9 + 7
        for i in range(1, 27): mp[str(i)] = 1
        for i in range(10): mp["*" + str(i)] = 1 + (i < 7) # 预处理
        mp["*"], mp["**"], mp["1*"], mp["2*"] = 9, 15, 9, 6 
        dp2 = 1; dp1 = mp[s[0]]
        for i in range(1, len(s)):
            dp = dp1 * mp[s[i]] + dp2 * mp[s[i - 1] + s[i]] % M
            dp2, dp1 = dp1, dp
        return dp1 % M
def main():
    solution = Solution()  
    s  = "*1*1*0"
    out = solution.preprocess(s)
    print(out) 

if __name__ == "__main__":
    main()

# 96
