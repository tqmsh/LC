from typing import List 
from collections import deque, defaultdict

class Solution:
    def _dfs(self, u, target, path, e, vis, ans):
        if u == target: 
            ans[0] = min(ans[0], path)
            return
        vis.add(u)
        for v, w in e[u]:
            if v not in vis:
                # vis.add(v)
                self._dfs(v, target, path * w, e, vis, ans)
                # vis.remove(v)
        vis.remove(u)

    def currency_converter(self, a, s, t):
        e = defaultdict(list)
        ans = [float('inf')]
        vis = set()
        for x in a:
            u, v, w = x.split(',')
            e[u].append((v, float(w)))
        self._dfs(s, t, 1.0, e, vis, ans)  
        return -1.0 if ans[0] == float('inf') else ans[0]
def main(): 
    solution = Solution() 
    currencies_input_1 = [
        "USD,CAD,1.3",
        "USD,GBP,0.71",
        "USD,JPY,109",
        "GBP,JPY,155",
        "CAD,GBP,0.55",
        "CAD,JPY,100"
    ]
    currency_from_1 = "USD"
    currency_to_1 = "JPY" 
    out = solution.currency_converter(currencies_input_1, currency_from_1, currency_to_1) 
    print(out) 

if __name__ == "__main__":
    main()