from math import factorial
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        M = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range (1, goal + 1):
            for j in range (1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % M + dp[i - 1][j] * max(0, j - k) % M
        return dp[goal][n] % M
    def numMusicPlaylists_compressed(self, n: int, goal: int, k: int) -> int:
        M = 10 ** 9 + 7
        prev_dp = [0] * (goal + 1)
        prev_dp[0] = 1
        dp = [0] * (goal + 1)
        for i in range (1, goal + 1):
            for j in range (1, n + 1):
                dp[j] = prev_dp[j - 1] * (n - j + 1) % M + prev_dp[j] * max(0, j - k) % M
            prev_dp, dp = dp, [0] * (goal + 1)
        return prev_dp[n] % M
    def numMusicPlaylists_optimized(self, n: int, goal: int, k: int) -> int:
        M = 10 ** 9 + 7
        prev_dp = [0] * (goal + 1)
        dp = [0] * (goal + 1)
        for i in range (k + 1, goal + 1):
            if i == k + 1:
                prev_dp[k + 1] = factorial(n) // factorial(n - i) # arrangement of i item from n item
            else:
                for j in range (k + 1, n + 1):
                    dp[j] = prev_dp[j - 1] * (n - j + 1) % M + prev_dp[j] * (j - k) % M
                prev_dp, dp = dp, [0] * (goal + 1)
        return prev_dp[n] % M

n = 2; goal = 3; k = 1
print(Solution().numMusicPlaylists_optimized(n, goal, k))