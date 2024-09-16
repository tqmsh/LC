from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
import re

class Solution: 
    def pourWater(self, heights, V, K):
        for _ in range(V):
            # 左边卡位
            j_l = K
            while (j_l - 1) >= 0 and heights[j_l - 1] <= heights[j_l]: j_l -= 1
            while (j_l + 1) <= K and heights[j_l + 1] == heights[j_l]: j_l += 1
            j_r = K
            while (j_r + 1) < len(heights) and heights[j_r + 1] <= heights[j_r]: j_r += 1
            while (j_r - 1) >= K and heights[j_r - 1] == heights[j_r]: j_r -= 1
            # 左边卡位成功
            if heights[j_l] < heights[K]: heights[j_l] += 1
            # 用右边卡位结果
            else: heights[j_r] += 1  
        return heights
def main():
    solution = Solution()  
    nums = [2,1,1,2,1,2,2]
    V = 4; K = 3
    out = solution.pourWater(nums, V, K)
    print(out) 

if __name__ == "__main__":
    main()
