from typing import (
    List,
)

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        n, m = len(matrix), len(matrix[0])
        x, y = 0, 0; d = 1; ans = []
        while x < n and y < m: 
            ans.append(matrix[x][y]) 
            nx = x + (-1 if d == 1 else 1)
            ny = y + (1 if d == 1 else -1) 
            if nx < 0 or nx == n or ny < 0 or ny == m: 
                if d: 
                    x += (y == m - 1)
                    y += (y < m - 1)
                else: 
                    y += (x == n - 1)
                    x += (x < n - 1) 
                d = 1 - d        
            else:
                x = nx
                y = ny 
        return ans