from typing import List
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int: 
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for c_i, w_i in zip(time, cost):
            c_i += 1 # 不仅自己杀 c_i 空间单位 (墙)，自己也解决了
            for j in reversed(range(n + 1)): dp[j] = min(dp[j], dp[max(0, j - c_i)] + w_i) 
        return dp[n]

cost = [1,2,3,2]; time = [1,2,3,2]
print(Solution().paintWalls(cost, time))