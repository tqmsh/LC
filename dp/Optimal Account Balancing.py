from collections import defaultdict
class Solution:
    def _isok(self, x, d):
        sum = 0; cnt = 0
        for i in range(len(d)):  
            if (1 << i) & x: 
                sum += d[i]
                cnt += 1
        return (sum == 0, cnt)

    def minTransfers(self, transactions):
        d = defaultdict(int)
        for u, v, w in transactions:
            d[u] -= w; d[v] += w
        d = [v for v in d.values() if v]; n = len(d)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0 # 啥不选，本身已经合法，无需多余
        for i in range(1, 1 << n):
            f, cnt = self._isok(i, d) # 递归条件 (1) 本身可以被满足 (2) 最坏 & 小问题合并打擂台
            if f:
                dp[i] = cnt - 1
                for j in range(i):
                    if j & i == j: # j 是 i 的子集
                        dp[i] = min(dp[i], dp[j] + dp[i - j])
        return dp[-1]
print(Solution().minTransfers([(0,1,10), (2,0,5)]))



