from typing import List, Dict
from collections import defaultdict
class Solution:
    def _dfs(self, u: int, f: int, e: Dict[int, List[int]], s: str) -> List[str]:
        if u == 0: return [""] 
        ans = []
        for v in e[u]:  
            for path in self._dfs(v, u, e, s): 
                ans.append(path + s[v + 1: u + 1] + " ")
        return ans

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s); s = " " + s   
        dp = [0] * (n + 1)
        dp[0] = 1    
        word_set = set(wordDict)   
        max_len = max(len(word) for word in wordDict)   
        e = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j + 1: i + 1] in word_set:
                    dp[i] = 1
                    e[i].append(j)
                    
        if not dp[n]: return []
        return [s[:len(s) - 1] for s in self._dfs(n, -1, e, s)]

# Example usage:
solution = Solution()
print(solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) 