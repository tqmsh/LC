import collections
from typing import List

class TrieNode:
    def __init__(self, x = -1):
        self.children = collections.defaultdict(TrieNode)
        self.x = x

class Trie:
    def __init__(self): self.root = TrieNode() 
    def insert(self, path, x):
        now: TrieNode = self.root 
        for i in range(len(path)): 
            now = now.children[path[i]] 
            if now.x == -1 and i != len(path) - 1: return 0
        now.x = x; return 1
    def search(self, path):
        now: TrieNode = self.root 
        for i in range(len(path)): 
            now = now.children[path[i]] 
            if now.x == -1: return -1
        return now.x

class FileSystem:
    def __init__(self): self.trie: Trie = Trie()
    def createPath(self, path: str, x): return(self.trie.insert(path.split('/')[1:], x))
    def get(self, path: str): return(self.trie.search(path.split('/')[1:]))

def main():
    # Initialize the FileSystem
    fileSystem = FileSystem()
    
    # Test case 1
    commands1 = [
        ["FileSystem"],
        ["createPath", "/a", 1],
        ["get", "/a"]
    ]
    expected1 = [None, True, 1]
    run_test(fileSystem, commands1, expected1)
    
    # Test case 2
    fileSystem = FileSystem()  # Reinitialize for a fresh start
    commands2 = [
        ["FileSystem"],
        ["createPath", "/leet", 1],
        ["createPath", "/leet/code", 2],
        ["get", "/leet/code"],
        ["createPath", "/c/d", 1],
        ["get", "/c"]
    ]
    expected2 = [None, True, True, 2, False, -1]
    run_test(fileSystem, commands2, expected2)

def run_test(fileSystem, commands, expected):
    results = []
    for command in commands:
        if command[0] == "FileSystem":
            results.append(None)
        elif command[0] == "createPath":
            path, value = command[1], command[2]
            results.append(fileSystem.createPath(path, value))
        elif command[0] == "get":
            path = command[1]
            results.append(fileSystem.get(path))
    print(results == expected, results)

if __name__ == "__main__":
    main()
