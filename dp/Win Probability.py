from functools import lru_cache
class Solution:
    @lru_cache(None)
    def _dp(self, i):
        if self.a <= i <= self.b: return 1
        if i > self.b: return 0
        ans = 0.0
        for x in range(1, self.N + 1): ans += self._dp(i + x) / self.N
        return ans
    def win_probability(self, N, a, b):
        self.N = N; self.a = a; self.b = b
        return self._dp(0)
    def win_probability_dp(self, N, a, b):
        dp = [0] * (b + N + 1)
        for i in range(a, b + 1): dp[i] = 1
        for i in range(a - 1, -1, -1): dp[i] = sum(dp[i + 1:i + N + 1]) / N
        return dp[0]
print(Solution().win_probability(6,4,8))