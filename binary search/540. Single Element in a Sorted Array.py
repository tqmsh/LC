from typing import List 
from collections import defaultdict
class Solution: 
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2  
            if (mid - 1 < 0 or nums[mid] != nums[mid - 1]) and (mid + 1 > len(nums) - 1 or nums[mid] != nums[mid + 1]): 
                return nums[mid]
            if (mid - 1 >= 0 and nums[mid] == nums[mid - 1] and mid % 2 == 0) or (mid + 1 < len(nums) and nums[mid] == nums[mid + 1] and mid % 2 != 0):
                r = mid - 1
            else:
                l = mid + 1 
        return 1 
def main():
    solution = Solution()  
    arr = [1,1,2]
    out = solution.singleNonDuplicate(arr)
    print(out) 

if __name__ == "__main__":
    main()
