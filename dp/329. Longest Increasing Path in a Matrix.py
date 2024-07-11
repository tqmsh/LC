from typing import List 
from collections import defaultdict
import math
class Solution:
    # Edge Top Sort 模版
    def _top_sort(self, e):
        n = len(e); inn = [0] * n 
        for u in range(n):
            for v, _ in e[u]:
                inn[v] += 1 
        q = [u for u in range(n) if inn[u] == 0]
        ans = [] 
        while q:
            u = q.pop(0)
            ans.append(u)
            for v, _ in e[u]:
                inn[v] -= 1
                if inn[v] == 0:
                    q.append(v) 
        return ans
    
    def longest_path_DAG(self, e, rt):
        dp = [float('-inf')] * len(e)
        dp[rt] = 0
        # DAG 图整个变成一个数
        top_sort_order = self._top_sort(e)
        for u in top_sort_order:
            for v, w in e[u]:
                dp[v] = max(dp[v], dp[u] + w)
        return max(dp)
def main():
    solution = Solution()  
    adj = [[] for i in range(4)]  
    adj[0].append([1, 1]) 
    adj[0].append([2, 100])
    adj[1].append([2, 1])
    adj[2].append([3, 1])
    out = solution.longest_path_DAG(adj, 0)
    print(out) 

if __name__ == "__main__":
    main()
