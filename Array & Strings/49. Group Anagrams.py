from typing import List
from collections import Counter
from collections import defaultdict

class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        mp = defaultdict(list)
        for x in strs:
            # sorted 模版
            sorted_word = ''.join(sorted(x)) 
            mp[sorted_word].append(x)
        
        ans = []
        for k, v in mp.items():
            ans.append(v)
        return ans
            
    
def main():
    solution = Solution() 
    out = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(out) 

if __name__ == "__main__":
    main()