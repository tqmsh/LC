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
    def _check(self, x, y, grid): # 没有越界，没有走过，不是障碍
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0   
        if not (grid[x][y] == 1): return 0
        return 1  
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        
        ans = []
        dirx = [0, 0, -1, 1]
        diry = [-1, 1, 0, 0]
        for x, y in hits: grid[x][y] -= 1
        
        # init
        f = {}; sz = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    f[(i, j)] = (i, j)
                    sz[(i, j)] = 1
        f['roof'] = 'roof'; sz['roof'] = 0
 
        # merge 
        for j in range(len(grid[0])): 
            if grid[0][j] == 1: self._merge((0, j), 'roof', f, sz)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    for k in range(4):
                        nx = x + dirx[k]
                        ny = y + diry[k] 
                        if self._check(nx, ny, grid): self._merge((x, y), (nx, ny), f, sz) 
        # connect
        for x, y in reversed(hits):
            grid[x][y] += 1
            if grid[x][y] != 1: 
                ans.append(0)
                continue
            f[(x, y)] = (x, y)
            sz[(x, y)] = 1 

            ini = sz[self._find('roof', f)]
            if x == 0: self._merge((x, y), 'roof', f, sz)
            for i in range(4):
                nx = x + dirx[i]
                ny = y + diry[i] 
                if self._check(nx, ny, grid): self._merge((nx, ny), (x, y), f, sz) 
            fin = sz[self._find('roof', f)]
            ans.append(max(0, fin - ini - 1))
        return list(reversed(ans))
    
grid = [[0,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[0,0,0,1,0,0,1,1,1],[0,0,1,1,0,1,1,1,0],[0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,1,0]]
hits = [[1,8],[2,1],[1,4],[3,0],[3,4],[0,7],[1,6],[0,8],[2,5],[3,2],[2,0],[0,2],[0,5],[0,1],[4,8],[3,7],[0,6],[5,7],[5,3],[2,6],[2,2],[5,8],[2,8],[4,0],[3,3],[1,1],[0,0],[4,7],[0,3],[2,4],[3,1],[1,0],[5,2],[3,8],[4,2],[5,0],[1,2],[1,7],[3,6],[4,1],[5,6],[0,4],[5,5],[5,4],[1,5],[4,4],[3,5],[4,6],[2,3],[2,7]]
print(Solution().hitBricks(grid, hits))