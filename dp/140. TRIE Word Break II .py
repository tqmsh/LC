import collections
from typing import List

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            curr = curr.children[char]
            if curr.end and char != word[-1]:
                return False
        return curr.end
class Solution:
    def _bfs(self, s, trie: Trie, ans):
        stk = [(s, "")]   
        while stk:
            now_req, now_path = stk.pop()
            if not now_req: ans.append(now_path.strip())
            now_node = trie.root
            i = 0
            while i < len(now_req) and now_req[i] in now_node.children:  # Search for matching words 
                now_node = now_node.children[now_req[i]]
                if now_node.end:  
                    word = now_req[:i + 1]
                    nxt_req = now_req[i + 1:]
                    nxt_path = now_path + ' ' + word
                    stk.append((nxt_req, nxt_path))
                i += 1

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]: 
        # Create a Trie and insert all words from the wordDict
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        ans = []
        self._bfs(s, trie, ans)
        return ans


# Example usage:
solution = Solution()
print(solution.wordBreak("bb", ["a","b","bbb","bbbb"]))
print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) 