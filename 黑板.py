from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort() 
        l = len(nums[::2])
        nums[::2], nums[1::2] = nums[:l][::-1], nums[l:][::-1]
a = [1,2,3,4,5,6,7,8,9]
Solution().wiggleSort(a)
print(a)