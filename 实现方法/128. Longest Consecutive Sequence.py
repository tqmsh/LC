from typing import List
from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set 去重
        nums = set(nums) 
        mp = {} 
        # mp[i]: 用 i 当区间段点时，区间最优值
        
        # len = mp[i + 1] + mp[i - 1] + 1       -------i------- -> 整段区间最优值 = 和
        # mp[i - mp[i - 1]] = len              (-)------i-------
        # mp[i + mp[i + 1]] = len
        ans = 0
        for n in nums: 
            l, r = mp.get(n - 1, 0), mp.get(n + 1, 0)
            len = l + r + 1  
            mp[n - l] = len
            mp[n + r] = len
            ans = max(ans, len) 
        return ans 

        
    
def main():
    solution = Solution() 
    nums = [100,4,200,1,3,2]
    out = solution.longestConsecutive(nums)
    print(out) 

if __name__ == "__main__":
    main()