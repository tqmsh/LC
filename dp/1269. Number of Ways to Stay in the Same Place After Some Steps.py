
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MXJ = min(steps // 2, arrLen - 1) # 0 indexed
        M = 10**9+7
        dp = [0] * (MXJ + 1)
        dp[0] = 1 # for i = 0, 0 steps taken, dont do anything, be at 0, ways = 1
        for i in range(1, steps + 1):
            lst = 0
            for j in range(MXJ + 1): 
                dp[j], lst = lst + dp[j] + (dp[j + 1] if j + 1 <= MXJ else 0), dp[j]
        return dp[0] % M
    
print(Solution().numWays(4, 2))