from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self): 
        self.children: defaultdict[str, TrieNode] = defaultdict(TrieNode) 
        self.end = 0 
        self.val = []

class Trie:
    def __init__(self): self.root: TrieNode = TrieNode()
    
    def insert(self, path, end = 0, val = None): 
        now = self.root
        for p in path: now = now.children[p]
        now.end = end
        if val: now.val.append(val)

    def search(self, path):  
        now = self.root
        for p in path:
            if p not in now.children: return None
            now = now.children[p]
        return now

class FileSystem:
    def __init__(self): self.trie: Trie = Trie()

    def mkdir(self, path: str): self.trie.insert(path.strip('/').split('/'))

    def ls(self, path: str):
        path = path.strip('/').split('/') if path != '/' else []
        node = self.trie.search(path)
        if not node: return [] # 字典树不存在这个节点
        if node.end: return path[-1] # 这个节点是叶子，不存在儿子，所以直接把这个节点所对应的字母给出来
        return sorted(node.children.keys()) # 存在这个节点

    def addContentToFile(self, path: str, val): 
        self.trie.insert(path.strip('/').split('/'), end = 1, val = val)

    def readContentFromFile(self, path: str) -> str:  
        node = self.trie.search(path.strip('/').split('/'))
        # /a/b/d/c/ -> strip -> a/b/c/d -> split -> a b c d
        return node.val
# --- Test Execution ---

fs = FileSystem()
print(fs.ls("/"))  # Output: []
print(fs.mkdir("/a/b"))
print(fs.addContentToFile("/a/b/c/d", "hello"))
print(fs.addContentToFile("/a/b/c/d", "hhiii"))
print(fs.ls("/a/b/c/d"))  # Output: ["a"]
print(fs.readContentFromFile("/a/b/c/d"))  # Output: "hello"
