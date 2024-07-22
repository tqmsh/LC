from typing import List 
from collections import defaultdict 
import math
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int: 
        dp = [[0] * (len(matrix[0])) for _ in range(len(matrix))] 
        for i in range(len(matrix)): 
            if matrix[i][0]: dp[i][0] = 1 
        for j in range(len(matrix[0])): 
            if matrix[0][j]: dp[0][j] = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]: dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 

        return sum(sum(r) for r in dp)

        
def main():
    solution = Solution()  
    matrix = [
    [1,0,1],
    [1,1,0],
    [1,1,0]
    ]
    out = solution.countSquares(matrix)
    print(out) 

if __name__ == "__main__":
    main()
