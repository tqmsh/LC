from typing import List
from collections import Counter

class Solution: 
    def nextPermutation(self, nums: List[int]) -> None:
        # 产生贡献位置，能晚一点，则晚一点; 用最靠右的位置产生非零贡献
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]: i -= 1

        
        if i != -1:
            # 答案枚举优化，第一 > num[i], 可用的，就是最小合法 
            ans = -1; l = i + 1; r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > nums[i]:
                    ans = mid
                    l = mid + 1
                else: r = mid - 1 
            nums[i], nums[ans] = nums[ans], nums[i]  
            
        # 最小化 i 位置的贡献的前提上，[i+1, n] 也尽量最小化
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums
    

def main():
    solution = Solution()
    nums = [1,1,5]
    out = solution.nextPermutation(nums)
    print(out) 

if __name__ == "__main__":
    main()