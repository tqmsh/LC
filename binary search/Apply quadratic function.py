from typing import List 
from collections import defaultdict
class Solution:
    # 最小化最大值，l 越大，|a[l] - x| 越小，越容易满足 |a[l] - x| < |a[l + k] - x| 的要求  
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        nums = [x ** 2 * a + x * b + c for x in nums] 
        ans = [0] * len(nums)
        i = 0; j = len(nums) - 1
        x, dx = (i, 1) if a < 1 else (j, -1) 
        while i <= j:
            if nums[i] * dx < nums[j] * dx: # dx > 0 从小到大，< 0 从大到小
                ans[x] = nums[i] 
                i += 1
            else:
                ans[x] = nums[j]
                j -= 1
            x += dx
        return ans

    
def main():
    solution = Solution()  
    nums = [-4,-2,2,4]
    a = 1
    b = 3
    c = 5 
    out = solution.sortTransformedArray(nums, a, b, c)
    print(out) 

if __name__ == "__main__":
    main()
