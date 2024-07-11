from typing import List 
from math import ceil
class Solution:
    def _is_possible(self, mid, piles, h): 
        req_h = 0
        for pile in piles: req_h += ceil(pile/mid)
        return req_h <= h
    
    # 最小化最大值，二分答案 
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        left = 1; right = max(piles); ans = 0 # 1e9 会精度问题， left = 1 会 division by 0
        while left <= right:
            mid = (left + right) // 2
            if self._is_possible(mid, piles, h):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
def main():
    solution = Solution()  
    piles = [3,6,7,11]; h = 8 
    out = solution.minEatingSpeed(piles, h)
    print(out) 

if __name__ == "__main__":
    main()
