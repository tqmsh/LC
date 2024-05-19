from typing import List
from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 贪心，位置能近一点，则近一点; 用最小的位置差，判断 k 是否合法
        mp = {} #val -> last i

        # 边枚举边计算
        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True     

            mp[nums[i]] = i

        return False
        
    
def main():
    solution = Solution() 
    out = solution.containsNearbyDuplicate([1,2,3,1,2,3], 2)
    print(out) 

if __name__ == "__main__":
    main()