from typing import List
from bisect import bisect_left
from collections import defaultdict
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        
        s = " " + s
        cnt = defaultdict(int) # 初始化 [0, 0) 
        L = [1] * len(s); psa = [0] * len(s)

        # 双指针, Sliding Window
        j = 1
        for i in range(1, len(s)): 
            cnt[s[i]] += 1
            while cnt['0'] > k and cnt['1'] > k: cnt[s[j]] -= 1; j += 1 # xxxxxxxx(v)vvvvvvv

            # cnt: [j, i]
            
            L[i] = j
            psa[i] = psa[i - 1] + (i - j + 1) # [j, i], 里面任何一个数，以 i 结尾，都是合法区间
        ans = []
        # 二分，枚举 R 找 L
        for l, r in queries:
            l += 1; r += 1 
            mn_R = bisect_left(L, l, l, r + 1) # [l, r + 1) 里第一个 idx, L[idx] >= l  
            ans.append((mn_R - l) * (mn_R - l + 1) // 2 + psa[r] - psa[mn_R - 1])
            # [l, mn_R) 所有子区间合法                     # 剩下的 R = [mn_R, r]  
        return ans
print(Solution().countKConstraintSubstrings("010101", 1, [[0,5], [1, 4], [2,3]]))