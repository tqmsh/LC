from typing import List 
from collections import defaultdict
import math
class Solution: 
    def shortest_distance(self, words, word1, word2):
        last_first = -1
        last_second = -1
        ans = 0
        for i, word in enumerate(words): 
            if word == word1:
                last_first = i
                if last_second != -1: ans = max(ans, last_first - last_second)
                
            if word == word2: 
                last_second = i
                if last_first != -1: ans = max(ans, last_second - last_first)
               
        return ans
def main():
    solution = Solution()  
    words = ["practice", "makes", "perfect", "coding", "makes"] 
    word1 = "coding"; word2 = "practice"
    out = solution.shortest_distance(words, word1, word2)
    print(out) 

if __name__ == "__main__":
    main()
