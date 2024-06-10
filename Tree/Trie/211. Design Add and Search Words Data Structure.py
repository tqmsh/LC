import collections
from typing import List

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False
 
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        curr = self.root
        for i in range(len(path)):
            curr = curr.children[path[i]]
        curr.end = True

    def search(self, path):
        curr = self.root
        for i in range(len(path)):
            curr = curr.children[path[i]]
            if curr.end and i != len(path) - 1:
                return False
        return True

class WordDictionary: 
    def __init__(self):
        self.trie = Trie()   
        self.maxLength = 0

    def addWord(self, word: str) -> None:
        self.trie.insert(word)
        self.maxLength = max(self.maxLength, len(word))

    def search(self, word: str) -> bool:
        # 可行性剪枝条
        if len(word) > self.maxLength: return 0  
        # 进门前判断
        def dfs(i, f): 
            if word[i] == '.':
                if i == len(word) - 1: 
                    for x in range(ord('a'), ord('z')+1):    
                        if f.children[chr(x)] and f.children[chr(x)].end: return True 
                    return False
                for x in range(ord('a'), ord('z')+1):    
                    if f.children[chr(x)] and dfs(i + 1, f.children[chr(x)]): return True
                return False
            else:   
                if i == len(word) - 1:
                    if f.children[word[i]].end: return True
                    return False
                if not f.children[word[i]]: return False
                return dfs(i + 1, f.children[word[i]])  
 
        # return dfs(0, self.trie.root)  
    
        # 进门后判断
        def dfs(i, f): 
            if i == len(word): return f.end 
            if word[i] == '.':
                # char loop 模版
                for x in range(ord('a'), ord('z')+1):    
                    if f.children[chr(x)] and dfs(i + 1, f.children[chr(x)]): return True
                return False
            else:   
                if not f.children[word[i]]: return False
                return dfs(i + 1, f.children[word[i]])  
        return dfs(0, self.trie.root) 

        

def display_grid(array):
    for row in array:
        for element in row:
            print(f"{element}\t", end="")
        print()  # Newline after each row
    print('--------------------------------------------------------') 
def main():  
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad") 
    wordDictionary.addWord("dad") 
    wordDictionary.addWord("mad")  
    print(wordDictionary.search("pad"))
    print(wordDictionary.search("bad"))
    print(wordDictionary.search(".ad"))
    print(wordDictionary.search("b..")) 

if __name__ == "__main__":
    main()
