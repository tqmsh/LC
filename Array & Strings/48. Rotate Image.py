from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None: 
        # 矩阵纵向反转 模版
        l = 0
        r = len(matrix) -1
        while l < r: 
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
    
        # 矩阵转置 模版
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix
         
def main():
    solution = Solution()  
    matrix = [[1,2,3],[4,5,6],[7,8,9]] 
    out = solution.rotate(matrix)
    print(out) 

if __name__ == "__main__":
    main()
