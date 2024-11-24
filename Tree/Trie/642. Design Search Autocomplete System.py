from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.e = defaultdict(TrieNode)  
        self.f = 0 # 字符节点选择存频率 & 完整字符串
        self.val = ""  

class Trie:
    def __init__(self): self.rt = TrieNode() 
    def insert(self, s, f):
        u = self.rt # 模版，走 s, 至最后一个字符
        for c in s: u = u.e[c] 
        
        u.f += f  # 维持最后一个字符
        u.val = s

    def search(self, s):
        u = self.rt # 模版，走 s, 至最后一个字符
        for c in s: 
            if c not in u.e: return None # 走不到处理，选择返回不存在
            u = u.e[c]

        return u # 返回最后一个字符

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = Trie()
        for s, f in zip(sentences, times): self.trie.insert(s, f) # 维持最后一个字符
        self.q = []  # Current query

    def _store(self): 
        self.trie.insert(''.join(self.q), 1) 
        self.q = []

    def _dfs(self, u: TrieNode, ans: List[str]):
        if u.f > 0: ans.append((u.f, u.val)) # 每一个节点 拿字符串；
        # 和自动补全 II 不一样，自动补全 II 是 最后一个字符 -> 子序列 (正难则反，反向维持的)
        # 这里是 最后一个字符 -> 路径是那些词的前缀 (正向维持，有前缀之后，从上到下找，而不是所有的字符串，枚举前缀，存起来 O(1) 拿)
        for v in u.e.values(): self._dfs(v, ans) # 模版 树上 DFS
             
    def input(self, c: str) -> List[str]:
        if c == '#': self._store(); return []

        self.q.append(c)
        u = self.trie.search(''.join(self.q))
        if not u: return [] # 走 s 无法走到最后一个
            
        ans = []
        self._dfs(u, ans)
        ans.sort(key=lambda x: (-x[0], x[1])) # 频率降序，LEX 生序
        return [v for _, v in ans[:3]]


# Usage
obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
print(obj.input("i"))  # Should return ["i love you", "island", "i love leetcode"]
print(obj.input(" "))  # Should return ["i love you", "i love leetcode"]
print(obj.input("a"))  # Should return []
print(obj.input("#"))  # Should save "i a" and return []
print(obj.input("i a"))