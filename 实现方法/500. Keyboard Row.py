from typing import List
from collections import Counter

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for w in words:
            # .lower() 模版
            # set 模版
            s = set(w.lower()) #🟥小心大小写#
            a, b, c = 0, 0, 0
            for x in s: 
                if x in "qwertyuiop": a += 1
                elif x in "asdfghjkl": b += 1
                else: c += 1  
            if (a + b == 0) | (a + c == 0) | (b + c == 0):
                ans.append(w)
        return ans
    
def main():
    solution = Solution()
    
    arr = ["Alaska", "Hello" ,"Dad","Peace"]
    out = solution.findWords(arr)
    print(out) 

if __name__ == "__main__":
    main()