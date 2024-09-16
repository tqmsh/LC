from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
import re

class Solution: 
    def the_sumof_legal_set(self, a: List[int], k: int) -> int:
        # 双指针
        i, j = 0, len(a) - 1  
        ans = 0
        while i <= j:
            # 进门后判断，进门前不知道 ans 能否用 i & j，先进来 (包括 i == j)，另做判断，在处理
            if a[i] + a[j] > k: j -= 1
            else:
                ans += 2 ** (j - i) # 录以 i 结尾的子集
                i += 1 # 不以 i 结尾的，以后录
        return ans % 1000000007
    
def main():
    solution = Solution()  
    a=[3,2,5,7,9];k=10
    out = solution.the_sumof_legal_set(a, k)
    print(out) 

if __name__ == "__main__":
    main()
