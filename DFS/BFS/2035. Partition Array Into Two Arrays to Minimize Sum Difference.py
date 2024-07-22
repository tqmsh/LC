from typing import List  
from collections import defaultdict
from itertools import combinations
from bisect import bisect_left, bisect_right
class Solution:
    def _get_2_n(self, nums):
        # ans[k]: (n, k), 所有方法的和
        ans = defaultdict(list)
        # 枚举子集长度
        for k in range(len(nums) + 1):   
            # 拿所有这么长的子集
            for c in combinations(nums, k): ans[k].append(sum(c))   
        return ans

    def minimumDifference(self, nums: List[int]) -> int:
        # 2^n 填坑 模版
        n = len(nums)//2; tot = sum(nums); req_sum = sum(nums)//2; ans = float('inf')
        l_arr = self._get_2_n(nums[:n]) # O(2 ^ (n / 2))
        r_arr = self._get_2_n(nums[n:]) 
        
        # 对半枚举
        for k in range(n + 1): # 枚举左半边 2^n子集，按照子集长度枚举
            r_arr[max(0, n - k)] = sorted(r_arr[max(0, n - k)])
            for l_sum in l_arr[k]:
                # 枚举一半，直接算另一半
                req_r_sum = req_sum - l_sum
                id = bisect_left(r_arr[max(0, n - k)], req_r_sum) # 第一 >= req_r_sum 的, 长n - k的 r 子集和
                for i in [id - 1, id]: # 如果 = 的情况不存在，那么我们需要去查看 第一 > 1 以及 第一 < 1 的结果
                    if i < 0 or i >= len(r_arr[max(0, n - k)]): continue
                    r_sum = r_arr[max(0, n - k)][i]
                    ans = min(ans, abs(2 * l_sum + 2 * r_sum - tot))
        return ans
    
def main(): 
    solution = Solution() 
    nums = [3,9,7,3]
    out = solution.minimumDifference(nums) 
    print(out) 

if __name__ == "__main__":
    main()