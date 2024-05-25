from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]: 
        ans = []
        for i in range (1, len(grid) - 1):
            tmp = []
            for j in range(1, len(grid[0]) - 1):
                tmpp = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        tmpp = max(tmpp, grid[k][l])
                tmp.append(tmpp)
            ans.append(tmp)
        return ans

def main():
    solution = Solution()  
    grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]] 
    out = solution.largestLocal(grid)
    print(out) 

if __name__ == "__main__":
    main()
