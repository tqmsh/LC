from typing import List 
from collections import defaultdict
from math import ceil
class Solution:
    def _f(self, x):
        x += 26 * ceil((97 - x) / 26)
        return x
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = defaultdict(int)
        lst = 'z'; len = 0
        for c in s:
            if ord(c) == self._f(ord(lst) + 1): len += 1
            else: len = 1 
            dp[c] = max(dp[c], len)
            lst = c
        return sum(dp.values()) 
        
def main():
    solution = Solution()  
    s = "a"
    out = solution.findSubstringInWraproundString(s)
    print(out) 

if __name__ == "__main__":
    main()
