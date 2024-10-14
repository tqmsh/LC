from collections import deque
from typing import List

class Solution:
    def _check(self, x, y, board):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]): return 0 
        if board[x][y] == 1: return 0 
        return 1

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> int:
        q = deque([(ball[0], ball[1])])
        mn = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]; mn[ball[0]][ball[1]] = 0
        p = [[""] * len(maze[0]) for _ in range(len(maze))]
        
        while q:
            x, y = q.popleft()
            for dx, dy, ch in [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]:
                nx, ny = x, y
                tmp = mn[x][y]
                while self._check(nx + dx, ny + dy, maze) and (nx, ny) != (hole[0], hole[1]):
                    nx += dx; ny += dy; tmp += 1
                np = p[x][y] + ch
                if tmp < mn[nx][ny] or (tmp == mn[nx][ny] and np < p[nx][ny]):
                    mn[nx][ny] = tmp
                    p[nx][ny] = np
                    if (nx, ny) != hole: q.append((nx, ny))
        return -1 if p[hole[0]][hole[1]] == "" else p[hole[0]][hole[1]]


print(Solution().findShortestWay(
maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [0,1]
))
