from typing import List 
from collections import defaultdict
import math
class Solution:
    def diffBetweenTwoStrings(self, s: str, p: str) -> bool:
        s = " " + s
        p = " " + p

        # dp 初始化 模版
        dp = [[float('inf')] * (len(p)) for _ in range(len(s))]
        for i in range(len(s)): dp[i][0] = i 
        for j in range(len(p)): dp[0][j] = j

        # 状态转移
        for i in range(1, len(s)):
            for j in range(1, len(p)): 
                if s[i] == p[j]: dp[i][j] = dp[i - 1][j - 1] # 多出来的选择
                dp[i][j] = min(dp[i][j], min(dp[i - 1][j], dp[i][j - 1]) + 1)
        
        # 反推答案
        i = len(s) - 1; j = len(p) - 1; ans = [] 
        while i >= 1 and j >= 1:
            if i == 0:  # s已经全部配对完了，只能把剩下的加回来了
                ans.append('+' + p[j])
                j -= 1
            elif j == 0:  # 已经达到目标了，把 s 剩下的删除
                ans.append('-' + s[i])
                i -= 1
            elif s[i] == p[j]:  # dp[i][j] = dp[i - 1][j - 1] 
                ans.append(s[i])
                i -= 1
                j -= 1
            elif dp[i - 1][j] < dp[i][j - 1]:  # dp[i][j] = dp[i - 1][j] + 1，即删除
                ans.append('-' + s[i])
                i -= 1
            else:  # dp[i][j] = dp[i][j - 1] + 1，即增加
                ans.append('+' + p[j])
                j -= 1
        ans = list(reversed(ans))
        return ans 
                
                
def main():
    solution = Solution()  
    s = "ABCDEFG"; p = "ABDFFGH"
    out = solution.diffBetweenTwoStrings(s, p)
    print(out) 

if __name__ == "__main__":
    main()
