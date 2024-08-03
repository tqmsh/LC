from collections import defaultdict

# Represents a node in the trie
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)  # Dictionary to store child nodes
        self.end = False  # Marks the end of a word
        self.words = set()  # Stores the words that end at this node

# Represents the trie data structure
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
            if curr.end and i != len(path) - 1: return False  
        return True 
 
class Typeahead:
    def __init__(self, dictionary):
        self._root = TrieNode()  
        for word in dictionary:
            self.insert_trie(word, word)
            for i in range(len(word)):
                for j in range(i + 1, len(word) + 1): self.insert_trie(word[i:j], word) # i.e. abcd's substr = bc; logs b -> c, end = 1; words = real

    def insert_trie(self, word, real_word): # insert basically but abit diff
        cur = self._root
        for ch in word:
            cur = cur.children[ch]  
        cur.end = True  
        cur.words.add(real_word)  

    def search_trie(self, cur, result): # walked the whole substring, rn we go chekc out the rest n log the endpts. 
        if cur.end:
            result.extend(cur.words)  # Add words to the result list
        for child in cur.children.values():
            self.search_trie(child, result)  # Recursive call to collect words from child nodes

    # Searches for words based on a prefix
    def search(self, string):
        result = []
        cur = self._root
        for ch in string:
            if ch not in cur.children:
                return result  # If character is not found, return empty result
            cur = cur.children[ch]  # Navigate to the child node
        self.search_trie(cur, result)  # Collect words from the current node
        return list(set(result))  # Remove duplicates and return the result

# Test cases
if __name__ == "__main__":
    dict1 = ["ab", "ac"]
    ta1 = Typeahead(dict1)
    print(ta1.search("a"))  
 