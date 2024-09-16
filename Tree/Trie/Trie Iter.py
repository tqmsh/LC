import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False
        self.value = None 
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path, value):
        curr = self.root
        for i in range(len(path)):
            curr = curr.children[path[i]]
        curr.end = True
        curr.value = value   
        
    def search(self, path):
        """ Search the trie to ensure the full path exists """
        curr = self.root
        for i in range(len(path)):
            if path[i] not in curr.children:
                return None
            curr = curr.children[path[i]]
        if curr.end:
            return curr.value
        return None

class MyIter:
    def __init__(self, reader: str, rt: TrieNode):
        self.rt = rt
        self.reader = reader
        self.s = self.get_s()
        self.i = 0
    def get_s(self):
        ans = ""
        i = 0
        while i < len(self.reader):
            now = self.rt
            while i < len(self.reader) and self.reader[i] in now.children: # 走树
                now = now.children[self.reader[i]]
                i += 1
                if now.end: ans += now.value
        return ans
    def next(self):
        val = self.s[self.i]
        self.i += 1
        return val
    def hasNext(self): # has next = current i ok?
        return self.i <= len(self.s) - 1
        
# Helper function to build the complex test trie
def build_complex_test_trie():
    trie = Trie()

    # Insert overlapping paths and varied length strings
    trie.insert("A", "h")
    trie.insert("AB", "ha")
    trie.insert("ABC", "hello")
    trie.insert("ABCDE", "world")
    trie.insert("XYZ", "test")
    trie.insert("XY", "go")

    return trie

# Running Complex Test Case
reader_complex = "ABCDEXYZ"
trie_complex = build_complex_test_trie()
my_iter_complex = MyIter(reader_complex, trie_complex.root)

result_complex = []
while my_iter_complex.hasNext():
    result_complex.append(my_iter_complex.next())
print("".join(result_complex)) 
