from typing import List 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:    
        j = 0
        for i in range(len(matrix) - 1, -1, -1): 
            while j + 1 < len(matrix[0]) and matrix[i][j] < target:  
                j += 1
            if matrix[i][j] == target: return 1
        return 0


def main():
    solution = Solution()  
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    out = solution.searchMatrix(matrix, target)
    print(out) 

if __name__ == "__main__":
    main()
