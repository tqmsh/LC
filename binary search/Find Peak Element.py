from typing import List 
from collections import defaultdict
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0; r = len(nums) - 1; ans = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= nums[min(len(nums) - 1, mid + 1)]: 
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
    def findTroughElement(self, nums: List[int]) -> int:
        l = 0; r = len(nums) - 1; ans = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= nums[min(len(nums) - 1, mid + 1)]: 
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans 

def main():
    solution = Solution()  
    nums = [3,2,2,2,2,2,2,2,2,1,3]
    out = solution.findPeakElement(nums)
    out2 = solution.findTroughElement(nums)
    print(out, out2) 

if __name__ == "__main__":
    main()
