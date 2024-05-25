from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]: 
        cnt = 0
        vis, len, ans = 1, 1, []
        dir, curDir = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        curR, curC = rStart, cStart
        ans.append([curR, curC])

        # BFS
        while vis < rows * cols and cnt < 20:

            # 扩展 
            dx, dy = dir[curDir]
            # 走几步
            for i in range(len):   
                nxtR, nxtC = curR + dx, curC + dy 

                # 进门
                if (0 <= nxtR < rows) and (0 <= nxtC < cols): 
                    vis += 1
                    ans.append([nxtR, nxtC]) 
                curR = nxtR
                curC = nxtC
            
            # 每换两次方向，就多走一步，改变下次扩展方法
            curDir = (curDir + 1) % 4
            if curDir % 2 == 0:
                len += 1
        return ans
 
         
def main():
    solution = Solution()  
    rows = 1
    cols = 4
    rStart = 0
    cStart = 0
    out = solution.spiralMatrixIII(rows, cols, rStart, cStart)
    print(out) 

if __name__ == "__main__":
    main()
