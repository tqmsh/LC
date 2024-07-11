from typing import List 
from collections import defaultdict
class Solution:
    # 最小化最大值，l 越大，|a[l] - x| 越小，越容易满足 |a[l] - x| < |a[l + k] - x| 的要求 
    def _get_min_l(self, arr: List[int], k: int, x: int) -> List[int]: 
        left = 0
        right = len(arr) - k
        while left <= right:
            mid = (left + right) // 2  
            if mid + k >= len(arr) or x - arr[mid] <= arr[mid + k] - x: # 不用 abs, 因为默认a[l + k]是x右边的
                                                                        # ，如果a[l + k]比x小的话，肯定不ok
                ans = mid
                right = mid - 1 
            else: 
                left = mid + 1   
        return ans
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = self._get_min_l(arr, k, x)
        return arr[l: l + k] 
    
def main():
    solution = Solution()  
    arr = [1,1,2,2,2,2,2,3,3]; k = 3; x = 3
    out = solution.findClosestElements(arr, k, x)
    print(out) 

if __name__ == "__main__":
    main()
