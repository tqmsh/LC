from typing import List 
from collections import deque, defaultdict

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Solution:
    def _find(self, x, f):
        if f[x] == x: return x 
        f[x] = self._find(f[x], f) 
        return f[x]
    
    def _check(self, x: int, y: int, n: int, m: int) -> bool:
        if x < 0 or y < 0 or x >= n or y >= m: return 0   
        return 1
    
    def _merge(self, x, y, f): # 把 x 添到 y 下
        Fx = self._find(x, f)
        Fy = self._find(y, f)
        if Fx != Fy: f[Fx] = Fy 

    def numIslands2(self, n, m, operators):
        # 并查集 动态加点 
        islands = set(); f = {}; ans = []; path = 0
        dirx = [0, 0, -1, 1]
        diry = [-1, 1, 0, 0]
        
        for opt in operators:
            x = opt[0]; y = opt[1] 
            if (x, y) in islands: 
                ans.append(path)
                continue
            # 新点，初始化
            islands.add((x, y))
            f[(x, y)] = (x, y)
            new = 1
            for i in range(4):
                nx = x + dirx[i]
                ny = y + diry[i] 
                if self._check(nx, ny, n, m): 
                    if (nx, ny) in islands: 
                        self._merge((x, y), (nx, ny), f)
                        new = 0
            path += new
            ans.append(path)
        return ans

def main(): 
    solution = Solution() 
    n = 3; m = 3; A = [[0,0],[0,1],[2,2],[2,1]]
    out = solution.numIslands2(n, m, A) 
    print(out) 

if __name__ == "__main__":
    main()