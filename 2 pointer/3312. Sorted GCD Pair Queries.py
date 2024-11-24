from typing import List
from collections import Counter, defaultdict
from itertools import accumulate
from bisect import bisect_right
from math import comb

# 预处理所有除数
class Solution: 
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        cnt = Counter(nums)
        
        mx = max(nums)
        gcd_to_numPair = [0] * (mx + 1)
        # 正难则反，不能直接数对枚举，就反向枚举
        for gcd in range(mx, 0, -1): # 构造，从大到小枚举，这样的话确保用的值都是定好的值，不会被后面改变
            tmp = 0
            tmp = sum(cnt[x] for x in range(gcd, mx + 1, gcd)) # 枚举 所有 x y 能用的数， (x, y) = gcd, x, y ∈ [gcd, mx], x, y = k * gcd
            gcd_to_numPair[gcd] = comb(tmp, 2)


            # A and B = A + B - (A or B)
            # A = pair in gcd
            # B = pair in gcd * 2, gcd * 3, ...
            # fix, gcd = 2, counts (2, 4) (2, 4) (4, 4), which is A and B
            # A = (A and B) - B + (A or B) = (A and B) - B
            
            
            for gcd_multiples in range(2 * gcd, mx + 1, gcd): 
                gcd_to_numPair[gcd] -= gcd_to_numPair[gcd_multiples]

        psa = list(accumulate(gcd_to_numPair)) # 修正累计数组的来源
        return list(map(lambda x: bisect_right(psa, x), queries))

# Example usage and test cases
print(Solution().gcdValues([2, 3, 4], [0, 2, 2]))  # 输出测试案例
