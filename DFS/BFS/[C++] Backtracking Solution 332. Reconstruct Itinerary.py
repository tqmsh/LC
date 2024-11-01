from collections import defaultdict
from typing import List, Dict

class Solution:
    def _dfs(self, u: str, e: defaultdict[str, List[str]], ans: List[str]): 
        while e[u]: self._dfs(e[u].pop(), e, ans)  
        ans.append(u) # Append after all destinations are fully explored (post-order)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        e = defaultdict(list)
        # Reverse sort tickets to maintain lexicographical order with pop
        for u, v in sorted(tickets, reverse=True): e[u].append(v)
        ans = []
        self._dfs("JFK", e, ans)
        return ans[::-1]  # Reverse to get the correct order

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(Solution().findItinerary(tickets))