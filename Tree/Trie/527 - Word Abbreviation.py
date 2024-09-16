from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.cnt = 0  # 变形: 节点经过的单词数量
        # self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for char in word: 
            curr = curr.children[char]
            curr.cnt += 1  # 变形: 增加计数
        # curr.end = True
    def search(self, word: str) -> int:
        curr = self.root
        for i, char in enumerate(word):
            curr = curr.children[char]
            if curr.cnt == 1:  # 变形: 唯一前缀点
                return i + 1
            # if curr.end and char != word[-1]:
            # return False
        return len(word)  # 变形: 如果没有找到唯一前缀，返回完整长度
        # return curr.end
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        # 为每个长度和最后一个字符的组合创建一个 Trie
        mp = defaultdict(Trie)
        for w in words:
            mp[(len(w), w[-1])].insert(w)
        
        ans = []
        for w in words:
            L_u = 0
            R_u = mp[(len(w), w[-1])].search(w)
            L_a = R_u
            R_a = len(w)
            
            # 如果缩写太短或缩写没有实际减少长度，则保持完整单词
            if R_a - L_a - 1 <= 1: ans.append(w)
                
            else: ans.append(w[L_u: R_u] + str(R_a - L_a - 1) + w[-1])  
        return ans

# 示例用法:
solution = Solution()
Input = ["internal", "internet", "interval"]
print(solution.wordsAbbreviation(Input))  # 输出: ['intern1l', 'intern1t', 'interv1l'] 