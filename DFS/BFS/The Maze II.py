from collections import deque
from itertools import pairwise
from typing import List

class Solution:
    def _check(self, x, y, board): 
        # 没有越界，没有走过 (不管)，不是障碍
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]): return 0  
        if board[x][y] == 0: return 0 
        return 1 
    
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        q = deque([(start[0], start[1])])
        ans = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]
        ans[start[0]][start[1]] = 0
        dir = [-1, 0, 1, 0, -1]  # directions array for (dx, dy) pairs
        while q:
            x, y = q.popleft()
            
            for dx, dy in pairwise(dir):
                nx = x
                ny = y
                tmp = ans[x][y]
                while self._check(nx + dx, ny + dy, maze):
                    nx += dx
                    ny += dy
                    tmp += 1
                if tmp < ans[nx][ny]:  # Only add count once after moving
                    ans[nx][ny] = tmp
                    q.append((nx, ny))
        return -1 if ans[destination[0]][destination[1]] == float('inf') else ans[destination[0]][destination[1]]

# Test case
maze = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1]
]
start = [0, 0]
destination = [3, 4]

print(Solution().shortestDistance(maze, start, destination))
