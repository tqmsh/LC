from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
import re

class Solution: 
    def maxArea(self, height: List[int]) -> int:

        # 双指针
        i, j = 0, len(height) - 1  
        ans = 0
        while (i < j): 
            ans = max(ans, (j - i) * min(height[j], height[i])) 
            # 枚举优化，删除不必要的枚举；将高的移动没有意义，不可能更优，只移低的
            if (height[j] < height[i]): j -= 1
            else: i += 1
             
        return ans
                    
def main():
    solution = Solution()  
    height = [2,3,4,5,18,17,6]


    out = solution.maxArea(height)
    print(out) 

if __name__ == "__main__":
    main()
