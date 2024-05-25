from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
class Solution:
    def __init__(self):
        self.psa = []

    # 二维前缀和 模版
    def psa2d(self, mat: List[List[int]]):
        self.psa = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))] 
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                self.psa[i][j] = mat[i][j] + (self.psa[i-1][j] if i > 0 else 0) + (self.psa[i][j-1] if j > 0 else 0) - (self.psa[i-1][j-1] if i > 0 and j > 0 else 0)
    
    def getPsa2d(self, r1, r2, c1, c2):
        r2 = min(r2, len(self.psa) - 1)
        c2 = min(c2, len(self.psa[0]) - 1)
        
        total = self.psa[r2][c2]
        if r1 > 0:
            total -= self.psa[r1 - 1][c2]
        if c1 > 0:
            total -= self.psa[r2][c1 - 1]
        if r1 > 0 and c1 > 0:
            total += self.psa[r1 - 1][c1 - 1]
 
        return total
    
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        self.psa2d(mat)  
        for i in range(len(mat)): 
            for j in range(len(mat[0])):
                print(i, j, self.getPsa2d(i - k, i + k, j - k, j + k))
                mat[i][j] = self.getPsa2d(i - k, i + k, j - k, j + k)
        
        return mat


def main():
    solution = Solution()  
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    out = solution.matrixBlockSum(mat, k)
    print(out) 

if __name__ == "__main__":
    main()
