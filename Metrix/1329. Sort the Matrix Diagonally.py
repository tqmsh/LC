from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ans = []

        for i in range(len(mat)):
            r = i
            c = 0
            ans = [] 
            while r < len(mat) and c < len(mat[0]):
                ans.append(mat[r][c]) 
                r += 1
                c += 1
            ans = sorted(ans)
            r = i
            c = 0
            while r < len(mat) and c < len(mat[0]):
                mat[r][c] = ans[c] 
                r += 1
                c += 1

        for j in range(1, len(mat[0])):
            r = 0
            c = j
            ans = []
            while r < len(mat) and c < len(mat[0]):
                ans.append(mat[r][c]) 
                r += 1
                c += 1
            ans = sorted(ans)
            r = 0
            c = j
            while r < len(mat) and c < len(mat[0]):
                mat[r][c] = ans[r] 
                r += 1
                c += 1 
        return mat
                    
def main():
    solution = Solution()  
    mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]] 
    out = solution.diagonalSort(mat)
    print(out) 

if __name__ == "__main__":
    main()
