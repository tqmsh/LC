from typing import List 
from typing import Optional  
class Solution:
    def _dfs(self, u, f, e, n, ans, sz):
        sz[u] = 1  # 子树大小
        dp_u = 0
        for v in e[u]:
            if v == f: continue
            self._dfs(v, u, e, n, ans, sz)
            sz[u] += sz[v]
            dp_u = max(dp_u, sz[v]) 
        if ans[1] > max(dp_u, n - sz[u]) or (ans[1] == max(dp_u, n - sz[u]) and ans[0] > u): 
            ans[1] = max(dp_u, n - sz[u])
            ans[0] = u
    def getBarycentrePoint(self, n, x, y) -> int:
        e = [[] for _ in range(n + 1)]; sz = [0] * (n + 1)
        for i in range(len(x)):
            e[x[i]].append(y[i])
            e[y[i]].append(x[i])
        ans = [0, float('inf')]
        self._dfs(1, 0, e, n, ans, sz)
        return ans[0]
      
def main():
    sol = Solution()
    n = 6
    print(sol.getBarycentrePoint(6, [1, 1, 2, 2, 3], [2, 3, 4, 5, 6]))  # Output: 1
    print(sol.getBarycentrePoint(4, [1, 1, 2], [2, 3, 4]))  # Output: 1
    print(sol.getBarycentrePoint(5, [1, 1, 1, 4], [2, 3, 4, 5]))  # Output: 1
    print(sol.getBarycentrePoint(7, [1, 1, 2, 2, 3, 3], [2, 3, 4, 5, 6, 7]))  # Output: 1

if __name__ == "__main__":
    main()
