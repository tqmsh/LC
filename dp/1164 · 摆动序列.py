from typing import List 
from collections import defaultdict
import math
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        prev_dp1 = 1
        prev_dp2 = 1
        for i in range(1, len(nums)):
            dp1 = prev_dp1
            if nums[i - 1] < nums[i]: dp1 = max(dp1, prev_dp2 + 1)
            
            dp2 = prev_dp2
            if nums[i - 1] > nums[i]: dp2 = max(dp2, prev_dp1 + 1)
            
            prev_dp1 = dp1
            prev_dp2 = dp2
        return max(dp1, dp2)

def main():
    solution = Solution()  
    a = [1,17,5,10,13,15,10,5,16,8]
    out = solution.wiggleMaxLength(a)
    print(out) 

if __name__ == "__main__":
    main()
