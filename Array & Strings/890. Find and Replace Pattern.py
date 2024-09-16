from typing import List
from collections import defaultdict
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]: 
        ans = []
        for word in words:
            f = defaultdict(int)
            f_r = defaultdict(int)
            tmp = 1
            for i in range(len(word)):
                x = word[i]
                y = pattern[i]
                if (f[x] and f[x] != y) or (f_r[y] and f_r[y] != x): tmp = 0; break
                f[x] = y; f_r[y] = x
            if tmp: ans.append(word)
        return ans
    
words = ["mpp", "aqq","dkd","ccc"]; pattern = "abb"
print(Solution().findAndReplacePattern(words, pattern))