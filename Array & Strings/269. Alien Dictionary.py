from itertools import pairwise
from collections import defaultdict, deque
from typing import List
class Solution: 
    def _top_sort(self, letters: set, e: defaultdict[str, list], inn: defaultdict[str, int], ans: List):
        q = deque()
        for c in letters:
            if not inn[c]:
                q.append(c) 
        while q:
            u = q.popleft()
            ans.append(u)
            for v in e[u]:
                inn[v] -= 1
                if not inn[v]: q.append(v)  

    def _get_e(self, e: defaultdict[str, list], inn: defaultdict[str, int], words):
        for s, t in pairwise(words):
            for i in range(min(len(s), len(t))):
                u = s[i]; v = t[i]
                if u != v: 
                    print(u, v)
                    e[u].append(v)
                    inn[v] += 1
                    break 
            else: # else block runs only if the for loop finishes without hitting the break
                if len(s) > len(t): return 0 
        return 1
    def alienOrder(self, words: List[str]) -> str:
        letters = {c for word in words for c in word} 
        e = defaultdict(list)
        inn = defaultdict(int)
        ans = []
        if not self._get_e(e, inn, words): return ""
        self._top_sort(letters, e, inn, ans)
        if any(inn.values()): return ""
        return "".join(ans)
print(Solution().alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]))  # Expected output: "" (since it's an invalid input case)
