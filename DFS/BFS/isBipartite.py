from typing import List
from collections import defaultdict
class Solution:
    def _dfs(self, u, col, ans, cols, e):
        if not ans[0]: return
        cols[u] = col
        for v in e[u]:
            if not cols[v]: self._dfs(v, 3 - cols[u], ans, cols, e)
            else:
                if cols[u] + cols[v] == 3: continue # 合法
                else:
                    ans[0] = 0
                    return
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        ans = [1]; cols = defaultdict(int)        
        for i in range(n):
            if not cols[i] and ans[0]: self._dfs(i, 1, ans, cols, graph) 
        return ans[0]
            
graph = [[1,3],[0,2],[1,3],[0,2]]
print(Solution().isBipartite(graph))