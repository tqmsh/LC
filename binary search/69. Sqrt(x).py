from typing import List 
from collections import defaultdict

class Solution:  
    def mySqrt(self, x: int) -> int:
        l = 0; r = x; ans = -1
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
                
def main():
    solution = Solution()  
    x = 3
    out = solution.mySqrt(x)
    print(out) 

if __name__ == "__main__":
    main()
