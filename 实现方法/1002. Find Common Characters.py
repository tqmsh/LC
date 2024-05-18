from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # map bool 模版
        mp = Counter(words[0]) 
        
        for w in words[1:]:   
            mp &= Counter(w)  
            
        ans = []
        for x, f in mp.items():
            ans += [x] * f
        return ans

    
def main():
    solution = Solution()
    
    words = ["bella","labe","roller"]
    out = solution.commonChars(words)
    print(out) 

if __name__ == "__main__":
    main()