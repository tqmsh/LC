from typing import List 
from collections import deque

class Solution:
    def _dfs(self, x, path, ans, s): # a(x)a b(x)bbb c(x)cc
        if x == len(s): ans.append(path)
        for nx in range(x + 1, len(s) + 1):
            if s[x: nx]==s[x:nx][::-1]: # check
                self._dfs(nx, path + [s[x: nx]], ans, s)
        
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self._dfs(0, [], ans, s)
        return ans
        
def main(): 
    solution = Solution() 
    s = "aab"
   
    out = solution.partition(s) 
    print(out) 

if __name__ == "__main__":
    main()