# Question:
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence 
# from beginWord to endWord. Each adjacent pair of words in the sequence must differ by a single letter, and each word in the sequence 
# (except beginWord) must be in wordList.

# Input:
# The input consists of three elements: a string beginWord, a string endWord, and a list of strings wordList. The words are lowercase 
# English letters and wordList is a dictionary of words.

# Output:
# The output is an integer representing the number of words in the shortest transformation sequence from beginWord to endWord. If no such 
# sequence exists, the output is 0.


from typing import List 
from collections import deque
from string import ascii_lowercase
class Solution:
    def _bfs(self, beginWord, endWord, wordList):
        wordList = set(wordList) # vis 
        q = deque([(beginWord, 1)])   
        while q:
            cur_word, cur_step = q.popleft() 
            if cur_word == endWord:
                return cur_step

            # 扩散
            for i in range(len(cur_word)):
                # ascii_lowercase 模版
                for c in ascii_lowercase:
                    nxt_word = cur_word[:i] + c + cur_word[i + 1:]; nxt_step = cur_step + 1 
                    if nxt_word in wordList:
                        q.append((nxt_word, nxt_step))
                        wordList.remove(nxt_word) # vis[] = 1
        return 0
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        return self._bfs(beginWord, endWord, wordList)
    
def main(): 
    solution = Solution() 
    beginWord = "hit"; endWord = "cog"; wordList = ["hot","dot","dog","lot","log"]
   
    out = solution.ladderLength(beginWord, endWord, wordList) 
    print(out) 

if __name__ == "__main__":
    main()