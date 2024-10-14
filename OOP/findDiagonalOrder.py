from typing import (
    List,
)

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        n, m = len(matrix), len(matrix[0])
        i, j = 0, 0; dir = 1; ans = []
        while i < n and j < m:
            ans.append(matrix[i][j])
            
            # move along in the current diagonal depending upon
            # the current dir.[i, j] -> [i - 1, j + 1] if 
            # going up and [i, j] -> [i + 1][j - 1] if going down.
            new_i = i + (-1 if dir == 1 else 1)
            new_j = j + (1 if dir == 1 else -1)
            
            # Checking if the next element in the diagonal is within the
            # bounds of the matrix or not. If it's not within the bounds,
            # we have to find the next head. 
            if new_i < 0 or new_i == n or new_j < 0 or new_j == m:
                
                # If the current diagonal was going in the upwards
                # dir.
                if dir:
                    
                    # For an upwards going diagonal having [i, j] as its tail
                    # If [i, j + 1] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i + 1, j] becomes the next head
                    i += (j == m - 1)
                    j += (j < m - 1)
                else:
                    
                    # For a downwards going diagonal having [i, j] as its tail
                    # if [i + 1, j] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i, j + 1] becomes the next head
                    j += (i == n - 1)
                    i += (i < n - 1)
                    
                # Flip the dir
                dir = 1 - dir        
            else:
                i = new_i
                j = new_j
                        
        return ans