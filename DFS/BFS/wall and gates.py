from typing import List
from collections import defaultdict
class Solution:
    def _check(self, x, y, grid, vis):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0
        if vis[x][y] or grid[x][y] == 0: return 0
        if grid[x][y] == -1: return 0
        return 1
    def walls_and_gates(self, rooms: List[List[int]]):
        if not rooms: return [] # 🟥 Edge Case: 空
        n = len(rooms); m = len(rooms[0])
        q = []; vis = [[0] * m for _ in range(n)]
        dirx = [0, 0, 1, -1]; diry = [1, -1, 0, 0]
        
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0: q.append((i, j, 0))
        
        while q:
            now_x, now_y, now_step = q.pop(0) 
            vis[now_x][now_y] = now_step
            for i in range(4):
                nxt_x = now_x + dirx[i]
                nxt_y = now_y + diry[i]
                nxt_step = now_step + 1
                if self._check(nxt_x, nxt_y, rooms, vis):
                    q.append((nxt_x, nxt_y, nxt_step))
                    vis[nxt_x][nxt_y] = nxt_step
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 2147483647: rooms[i][j] = vis[i][j]
        return rooms
graph = [[]]
print(Solution().walls_and_gates(graph))