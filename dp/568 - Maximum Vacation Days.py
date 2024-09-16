from typing import List
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n, k = len(flights), len(days[0])
        prev_dp = [-float('inf')] * n
        prev_dp[0] = 0
        
        for i in range(k): 
            dp = [-float('inf')] * n
            for u in range(n):
                for f in range(n):
                    if u == f or flights[f][u]:
                        dp[u] = max(dp[u], prev_dp[f] + days[u][i])
            prev_dp = dp
        
        return max(prev_dp)

from functools import lru_cache
from typing import List
class Solution:
    @lru_cache(None)
    def _dp(self, u: int, i: int) -> int:
        if i == self.k: return 0
        ans = 0
        for v in range(self.n):
            if v == u or self.flights[u][v] == 1:
                ans = max(ans, self.days[v][i] + self._dp(v, i + 1))
        return ans

    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        self.flights = flights
        self.days = days
        self.n, self.k = len(flights), len(days[0])
        return self._dp(0, 0)
