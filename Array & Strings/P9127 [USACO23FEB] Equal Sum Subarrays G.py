from typing import List
from collections import Counter

class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {} # val -> id

        # 边枚举边计算
        for i in range(len(nums)):
            y = target - nums[i]
            if y in mp:
                return [i, mp[y]]
            mp[nums[i]] = i
        
# s_b[mx[0]:mx[1] + 1].decode()

    
def main():
    solution = Solution()
    
    nums = [2,7,11,15]
    target = 9
    out = solution.twoSum(nums, target)
    print(out) 

if __name__ == "__main__":
    main()