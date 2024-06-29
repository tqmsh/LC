from typing import List 
from collections import defaultdict
import math
class WordDistance:
    def __init__(self, words):
        self.wordInd = {}
        for i, word in enumerate(words):
            if word in self.wordInd:
                self.wordInd[word].append(i)
            else:
                self.wordInd[word] = [i]

    def shortest(self, word1, word2):
        idx1 = self.wordInd[word1]
        idx2 = self.wordInd[word2]
        i, j, dist = 0, 0, float('inf')
        
        # 离散化 & 双指针
        while i < len(idx1) and j < len(idx2):
            dist = min(dist, abs(idx1[i] - idx2[j]))
            # 枚举优化，删除不必要的枚举；将高/低的移高/低没有意义，不可能更优，只移可能有帮助的的
            if idx1[i] < idx2[j]: i += 1 
            else: j += 1
            
        return dist 

def main():
    # Your WordDistance object will be instantiated and called as such:
    wordDistance = WordDistance(["practice", "makes", "perfect", "coding", "makes"] )
    print(wordDistance.shortest("practice", "perfect"))
    print(wordDistance.shortest("makes", "coding")) 

if __name__ == "__main__":
    main()
