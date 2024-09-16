from typing import List
from collections import Counter, defaultdict
from itertools import accumulate

class Solution: 
    def numFriendRequests(self, ages: List[int]) -> int:
        psa = [0] * 121
        cnt = Counter(ages)
        for v, f in cnt.items(): psa[v] += f
        psa = list(accumulate(psa))
        ans = 0
        for R in range(1, 121):
            if not cnt[R]: continue
            # 枚举 R 找 不合法 L 区间
            L_R = R // 2 + 7
            if L_R >= R: continue
            ans += (psa[R] - psa[L_R] - 1) * cnt[R]
                         # 自己不能给自己发
        return ans

def main():
    solution = Solution()
    ages = [20,30,100,110,120]
    out = solution.numFriendRequests(ages)
    print(out) 

if __name__ == "__main__":
    main()