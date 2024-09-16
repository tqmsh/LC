from collections import defaultdict
from typing import List
from itertools import pairwise, product
from functools import lru_cache
class Solution:
    @lru_cache
    def _dfs(self, now_lvl):
        if len(now_lvl) == 1: return 1
        tmp = []
        for x, y in pairwise(now_lvl):  tmp.append(self.e[(x, y)]) 
        for nxt_lvl in product(*tmp): 
            if self._dfs(nxt_lvl): return 1
        return 0
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.e = defaultdict(list)
        for s in allowed: self.e[(s[0], s[1])].append(s[2]) 
        return self._dfs(bottom) 
    
print(Solution().pyramidTransition(bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]))