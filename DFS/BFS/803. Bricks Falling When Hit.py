from typing import List

class Solution: 
    def _find(self, x, f):
        if f[x] == x: return x
        f[x] = self._find(f[x], f)
        return f[x]

    def _merge(self, x, y, f, sz):
        Fx = self._find(x, f)
        Fy = self._find(y, f)
        if Fx != Fy: 
            f[Fx] = Fy
            sz[Fy] += sz[Fx]  

    def _check(self, x, y, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0   
        if grid[x][y] != 1: return 0
        return 1  

    def hitBricks(self, grid: List[List[int]], hit: List[int]) -> List[int]:
        hit_x = hit[0]; hit_y = hit[1]
        dirx = [0, 0, -1, 1]
        diry = [-1, 1, 0, 0]

        grid[hit_x][hit_y] -= 1
        
        f = {}
        sz = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    f[(i, j)] = (i, j)
                    sz[(i, j)] = 1

        f['ground'] = 'ground'
        sz['ground'] = 0

        for j in range(len(grid[0])): 
            if grid[-1][j] == 1:
                self._merge((len(grid) - 1, j), 'ground', f, sz)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    for k in range(4):
                        nx = x + dirx[k]
                        ny = y + diry[k] 
                        if self._check(nx, ny, grid): 
                            self._merge((x, y), (nx, ny), f, sz) 

        grid[hit_x][hit_y] += 1
        if grid[hit_x][hit_y] != 1: return [0]

        f[(hit_x, hit_y)] = (hit_x, hit_y)
        sz[(hit_x, hit_y)] = 1 

        ini = sz[self._find('ground', f)]

        if hit_x == len(grid) - 1: 
            self._merge((hit_x, hit_y), 'ground', f, sz)
        
        for i in range(4):
            nx = hit_x + dirx[i]
            ny = hit_y + diry[i]
            if self._check(nx, ny, grid): 
                self._merge((nx, ny), (hit_x, hit_y), f, sz)

        fin = sz[self._find('ground', f)]
        return [max(0, fin - ini - 1)]
# Test case
grid = [
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0]
]
hits = [0, 2]
print(Solution().hitBricks(grid, hits))
