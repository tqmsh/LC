from typing import List 
from collections import deque, defaultdict

class Solution:
    def _find(self, x, f):
        if f[x] == x: return x 
        f[x] = self._find(f[x], f) 
        return f[x]
    
    def _check(self, x: int, y: int, grid) -> bool:
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0   
        return 1
    
    def _merge(self, x, y, f): # 把 x 添到 y 下
        Fx = self._find(x, f)
        Fy = self._find(y, f)
        if Fx != Fy: f[Fx] = Fy 

    def swimInWater(self, grid):
        if grid == [[0]]: return 0
        mp = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])): mp[grid[i][j]].append((i, j))
        
        # 并查集 
        f = {(i, j): (i, j) for i in range(len(grid)) for j in range(len(grid[0]))}
        avail = set() 
        dirx = [0, 0, -1, 1]
        diry = [-1, 1, 0, 0]

        for t in range(len(grid) * len(grid)):
            for x, y in mp[t]: 
                avail.add((x, y)) 
                for i in range(4):
                    nx = x + dirx[i]
                    ny = y + diry[i] 
                    if self._check(nx, ny, grid): 
                        if (nx, ny) in avail: self._merge((x, y), (nx, ny), f)
                        if self._find((0, 0), f) == self._find((len(grid) - 1, len(grid[0]) - 1), f): return t


def main(): 
    solution = Solution()  
    out = solution.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]) 
    print(out) 

if __name__ == "__main__":
    main()