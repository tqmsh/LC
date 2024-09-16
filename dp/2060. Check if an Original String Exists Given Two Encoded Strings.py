from typing import List 
from collections import defaultdict
from functools import lru_cache
class Solution:
    @lru_cache(None) # memo
    def _dfs(self, i, j, path, s1: str, s2: str): # path: e31e， path = 1: 可扩散至 e3ae, path = 31: 可扩散至 e a...a x 31 e
        n = len(s1); m = len(s2)
        if i == n and j == m and path == 0: return 1 # 坑全填好了，并且全合法

        # 直接过
        if i < n and j < m and path == 0 and s1[i] == s2[j] and self._dfs(i + 1, j + 1, path, s1, s2): return 1

        # e2e(i)x..., e3x(j)..., => e3x(i)..., e3x(j)...
        if i < n and not s1[i].isdigit() and path < 0 and self._dfs(i + 1, j, path + 1, s1, s2): return 1
        if j < m and not s2[j].isdigit() and path > 0 and self._dfs(i, j + 1, path - 1, s1, s2): return 1
        
        if path <= 0: # path 多种读取方式
            ptr = i; num = 0 
            while ptr < n and s1[ptr].isdigit(): 
                num = 10 * num + int(s1[ptr])
                if self._dfs(ptr + 1, j, path + num, s1, s2): return 1
                ptr += 1

        if path >= 0:
            ptr = j; num = 0 
            while ptr < m and s2[ptr].isdigit(): 
                num = 10 * num + int(s2[ptr])
                if self._dfs(i, ptr + 1, path - num, s1, s2): return 1 
                ptr += 1

        return 0
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        return self._dfs(0, 0, 0, s1, s2) == 1
def main():
    solution = Solution()  
    s1 = "a5b"; s2 = "c5b"

    out = solution.possiblyEquals(s1, s2)
    print(out) 

if __name__ == "__main__":
    main()
