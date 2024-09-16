from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
import re

class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num > 0: break # 必然 负/0 + (..) = 0     
            if i > 0 and nums[i] == nums[i - 1]: continue
            l = i + 1; r = len(nums) - 1 
            while l < r: # l == r 必然不合法
                sum = num + nums[l] + nums[r]
                if sum == 0: 
                    ans.append([num, nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: l += 1
                elif sum < 0: l += 1
                else: r -= 1 
        return ans

def main():
    solution = Solution()  
    nums = [-1,0,1,2,-1,-4] 
    out = solution.threeSum(nums)
    print(out) 

if __name__ == "__main__":
    main()
