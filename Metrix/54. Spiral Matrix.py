from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
class Solution:
    def _check(self, x, y, matrix):
        if not 0 <= x < len(matrix): return 0
        if not 0 <= y < len(matrix[0]): return 0
        if matrix[x][y] == '.': return 0
        return 1
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cur_x = 0; cur_y = 0; dx = 0; dy = 1
        ans = [] 

        for _ in range(len(matrix) * len(matrix[0])):
            # value = queue.pop() 
            ans.append(matrix[cur_x][cur_y]) #if value == requirements: results.append(value)  
            matrix[cur_x][cur_y] = '.' # 进队出有很多种情况 - 出队只有一种

            nxt_x = cur_x + dx; nxt_y = cur_y + dy  
            if self._check(nxt_x, nxt_y, matrix):
                cur_x = nxt_x
                cur_y = nxt_y
            else:
                # 该变方向
                dx, dy = dy, -dx  
                nxt_x = cur_x + dx; nxt_y = cur_y + dy  
                cur_x = nxt_x
                cur_y = nxt_y 
        return ans
    
    
  
def main():
    solution = Solution()  
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    out = solution.spiralOrder(matrix)
    print(out) 

if __name__ == "__main__":
    main()
