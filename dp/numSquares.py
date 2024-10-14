from math import sqrt
class Solution:
    def numSquares_dp(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(int(sqrt(n)) + 1):
            c_i = i * i; w_i = 1
            for j in range(c_i, n + 1): # j - c_i >= 0, j >= c_i
                dp[j] = min(dp[j], dp[j - c_i] + w_i)
        return dp[n]

    def _check(self, x, vis): 
        if x < 0: return 0  
        if x in vis: return 0
        return 1

    def numSquares_bfs(self, n: int) -> int:
        q = [(n, 0)] 
        vis = set([n])  
        while q:
            now, step = q.pop(0)
            if now == 0: 
                return step
            for i in range(1, int(sqrt(n)) + 1):
                nxt = now - i * i
                if self._check(nxt, vis):
                    vis.add(nxt)  
                    q.append((nxt, step + 1))  
        
print(Solution().numSquares_bfs(112))