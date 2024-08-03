from collections import defaultdict
from typing import List

# Trie 变形题
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = 0
        self.og = set() # Trie 基础上加出来的
    
class Trie:
    def __init__(self, dict): # Trie 基础上加出来的
        self.root = TrieNode()
        for s in dict:
            for i in range(len(s)): # 枚举子序列
                for j in range(i + 1, len(s) + 1): self.insert(s[i:j], s)
    def insert(self, path: str, ogg: str):  # Trie 基础上加出来的
        curr = self.root
        for i in range(len(path)): curr = curr.children[path[i]]
        curr.end = 1
        curr.og.add(ogg) # Trie 基础上加出来的
    def search(self, path: str) -> List[str]:
        curr = self.root
        for i in range(len(path)):
            if path[i] not in curr.children: return [] # Trie 基础上加出来的，走不全 substr 必然不合法
            curr = curr.children[path[i]]
        return curr.og # Trie 基础上加出来的, 满足 substr 要求即给出 og

dict1 = {"OpenAI is great", "OpenAI is good", "OpenAI research", "AI is the future", "Machine learning and AI"}
trie1 = Trie(dict1)

# Test searching for substrings with mixed cases and spaces
print(trie1.search("OpenAI"))  # Expected: ["OpenAI is great", "OpenAI is good", "OpenAI research"]
print(trie1.search("AI"))  # Expected: ["OpenAI is great", "OpenAI is good", "OpenAI research", "AI is the future", "Machine learning and AI"]
print(trie1.search("is"))  # Expected: ["OpenAI is great", "OpenAI is good", "AI is the future"]
print(trie1.search("Machine"))  # Expected: ["Machine learning and AI"]
