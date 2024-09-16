from typing import List
from collections import Counter

class Solution: 
    def totalFruit(self, fruits: List[int]) -> int:
        prev_prev, prev = -1, -1
        ans = float('-inf'); prev_2type_cnt = 0; prev_1type_cnt = 0
        for x in fruits:
            if x == prev: 
                prev_2type_cnt += 1
                prev_1type_cnt += 1
            if x != prev and x == prev_prev: 
                prev_2type_cnt += 1
                prev_1type_cnt = 1
            if x != prev and x != prev_prev:
                prev_2type_cnt = prev_1type_cnt + 1
                prev_1type_cnt = 1
            ans = max(ans, prev_2type_cnt, prev_1type_cnt)
            if x != prev: prev_prev, prev = prev, x
        return ans
                
def main():
    solution = Solution()
    
    fruits = [1,2,1,1,2]
    out = solution.totalFruit(fruits)
    print(out) 

if __name__ == "__main__":
    main()