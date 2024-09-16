from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
import re

class Solution: 
    def longestDupSubstring(self, s: str) -> str:
        j = 0
        ans = ""
        for i in range(len(s)): 
            while j < len(s) and s[i:j] in s[i+1:]:  
                if j - i > len(ans): ans = s[i:j]
                j += 1
        return ans          

def main():
    solution = Solution()  
    s = "baaaaaaaa"
    out = solution.longestDupSubstring(s)
    print(out) 

if __name__ == "__main__":
    main()



