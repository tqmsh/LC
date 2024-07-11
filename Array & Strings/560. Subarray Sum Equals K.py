from typing import List 
from collections import defaultdict
class Solution: 
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 枚举 R 找 L, 边枚举边计算
        psa = list(nums)
        cnt = defaultdict(int); cnt[0] = 1 # 出现次数
        ans = 0
        for i in range(1, len(psa)): psa[i] += psa[i - 1] 
        for sum in psa:
            ans += cnt[sum - k] # 以前遇到过可以与之匹配的
            cnt[sum] += 1 
        return ans


    
def main():
    solution = Solution()
    nums = [1,2,3]; k = 3
    out = solution.subarraySum(nums, k)
    print(out) 

if __name__ == "__main__":
    main()