from typing import List 
from typing import Optional  
class Solution:
    def _dfs_dp_sz(self, u, f, e, dp, sz):
        sz[u] = 1  # 子树大小
        for v, w in e[u]:
            if v == f: continue
            self._dfs_dp_sz(v, u, e, dp, sz)
            sz[u] += sz[v]
            dp[u] += dp[v] + sz[v] * w
    
    def _dfs_summ(self, u, f, e, dp, sz, summ, ans, n):
        for v, w in e[u]:
            if v == f: continue
            summ[v] = dp[v] + (summ[u] - dp[v] - sz[v] * w) + (n - sz[v]) * w
            if summ[v] < ans[0] or (summ[v] == ans[0] and v < ans[1]):
                ans[0] = summ[v]
                ans[1] = v
            self._dfs_summ(v, u, e, dp, sz, summ, ans, n)

    def getFermatPoint(self, n, u, v, w) -> int:
        e = [[] for _ in range(n + 1)]
        dp = [0] * (n + 1)
        sz = [0] * (n + 1)
        summ = [0] * (n + 1)
        
        for i in range(len(u)):
            e[u[i]].append((v[i], w[i]))
            e[v[i]].append((u[i], w[i]))
        
        self._dfs_dp_sz(1, 0, e, dp, sz)
        
        summ[1] = dp[1]
        ans = [summ[1], 1]
        self._dfs_summ(1, 0, e, dp, sz, summ, ans, n)
        return ans[1]
      
def main():
    solution = Solution()
    n = 5
    u = [1, 2, 2]
    v = [2, 3, 4]
    w = [1, 1, 1]
    out = solution.getFermatPoint(n, u, v, w) 
    print(out)
if __name__ == "__main__":
    main()
