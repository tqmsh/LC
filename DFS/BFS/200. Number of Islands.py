
from typing import List   
class Solution:
    def _check(self, x, y, vis, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0
        if (x, y) in vis: return 0
        if grid[x][y] == '0': return 0 
        return 1 
    
    def _dfs(self, x, y, vis, grid):
        dirx = [0,0,-1,1]
        diry = [-1,1,0,0]
        vis.add((x, y))
        for i in range(4):
            nx = x + dirx[i]
            ny = y + diry[i]
            if self._check(nx, ny, vis, grid):
                self._dfs(nx, ny, vis, grid)
        
    def numIslands(self, grid: List[List[str]]) -> int: 
        num_islands = 0
        vis = set()  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in vis:
                    num_islands += 1
                    self._dfs(i, j, vis, grid)  
        return num_islands

def main(): 
    solution = Solution() 
    digits = "23"
   
    out = solution.letterCombinations(digits) 
    print(out) 

if __name__ == "__main__":
    main()