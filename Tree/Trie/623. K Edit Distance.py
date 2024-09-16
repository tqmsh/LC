from typing import List
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.e = defaultdict(TrieNode)
        self.end = 0
        self.word = None
class Trie:
    def __init__(self): self.rt = TrieNode()
    def ins(self, a: List[str]):
        u = self.rt
        for x in a: u = u.e[x]
        u.end = 1; u.word = ''.join(map(str, a))
class Solution:
    def _dfs(self, prev_s_i_node: TrieNode, prev_dp, ans: List[str], t, k):
        if prev_s_i_node.end == 1: 
            if prev_dp[len(t) - 1] <= k: ans.append(prev_s_i_node.word); 
            return
        dp = [0] * len(t)
        dp[0] = prev_dp[0] + 1 # dp[i][0] = i <=> dp[0][0] = 0, dp[i][0] = dp[i - 1][0] + 1; 
        for s_i_ord in range(ord('a'), ord('z') + 1):
            s_i = chr(s_i_ord)
            if s_i not in prev_s_i_node.e: continue
            for j in range(1, len(t)): 
                if s_i == t[j]: dp[j] = prev_dp[j - 1]
                else: dp[j] = min(dp[j - 1], prev_dp[j - 1], prev_dp[j]) + 1
            self._dfs(prev_s_i_node.e[s_i], dp, ans, t, k)
    def kDistance(self, words: List[str], target: str, k: int):
        ans = []
        target = " " + target
        dp = [i for i in range(len(target))]
        trie = Trie()
        for word in words: trie.ins(word)
        self._dfs(trie.rt, dp, ans, target, k)
        return ans
print(Solution().kDistance(['acc', 'abcd', 'ade', 'abbcd'], 'abc', 2))