from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        path = Counter(s[:len(p) - 1])
        target = Counter(p)
        ans = []
        for i in range(len(p) - 1, len(s)):
            path[s[i]] += 1
            if path == target: ans.append(i - len(p) + 1)
            path[s[i - len(p) + 1]] -= 1
        return ans

print(Solution().findAnagrams("cbaebabacd", "abc"))