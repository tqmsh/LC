class Solution:
    def minCut(self, s: str) -> int:
        s = " " + s
        dp = [-1] + list(range(len(s))) # dp[0] = -1, 因为如果 j - 1 = -1, 那么就是整个是palin, 
                                        # 即 dp[i] = 0 = dp[j - 1] + 1, dp[j - 1] = -1
        isPalin = [0] + [1] * len(s) # 初始化 i = -1
        for i in range(1, len(s)):
            for j in range(1, i + 1):
                isPalin[j] =  (s[j] == s[i]) and (j + 1 == len(s) or isPalin[j + 1])
                if isPalin[j]: dp[i] = min(dp[i], dp[j - 1] + 1)
                # else case covered in init, which also covered basecase
        return dp[len(s) - 1]

print(Solution().minCut("ab"))