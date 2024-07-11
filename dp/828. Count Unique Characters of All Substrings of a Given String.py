from typing import List 
from collections import defaultdict
import math
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # 考虑s[i]字符对dp[i - 1]录的子串独特字母有何改变
        
        # 前1, 2 模版
        pre = defaultdict(lambda: (0, 0))
        ans = dp = 0
        for i, c in enumerate(s, 1):
            # 正难则反，减去多算的贡献
            dp = dp + i - pre[c][1] - (pre[c][1] - pre[c][0])
            # 子串已经见过 c 了          # 子串第一次见重复的 c, 本来与s[i-1]组合时合法的，现在变得变不合法了
            pre[c] = (pre[c][1], i)
            ans += dp
        return ans
def main():
    solution = Solution()  
    s = "LEETCODE"
    out = solution.uniqueLetterString(s)
    print(out) 

if __name__ == "__main__":
    main()
