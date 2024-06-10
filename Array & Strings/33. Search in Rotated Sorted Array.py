from typing import List 
import bisect

class Solution: 
    # fast
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid 

            if nums[left] <= nums[mid]: # 每一次尝试排除/采用具有单调性的一半 
                if nums[left] <= target < nums[mid]: right = mid - 1 
                else: left = mid + 1 
            else:
                if nums[mid] < target <= nums[right]: left = mid + 1 
                else: right = mid - 1  

        return -1
     

    # # lb, up 模版
    # def lower_bound(arr, target): # 第一 >= x
    #     return bisect.bisect_left(arr, target)

    # def upper_bound(arr, target): # 第一 > x
    #     return bisect.bisect_right(arr, target)

    # def search(self, nums: List[int], target: int) -> int:
    #     def find_pivot_index():
    #         left, right = 1, len(nums) - 1; pivot_index = 0
    #         while left <= right:
    #             mid = (left + right) // 2 
    #             if nums[mid] >= nums[0]:
    #                 left = mid + 1
    #             if nums[mid] < nums[0]:
    #                 pivot_index = mid
    #                 right = mid - 1 
    #         return pivot_index  
    #     pivot_index = find_pivot_index() 
    #     def binarySearch():  
    #         left, right = 0, len(nums) - 1
    #         while left <= right:
    #             mid = (left + right) // 2
    #             # 数学 
    #             rotated_index = (mid + pivot_index) % len(nums) 
    #             if nums[rotated_index] == target: return rotated_index 
    #             elif nums[rotated_index] < target: left = mid + 1 
    #             else: right = mid - 1 
    #         return -1  
    #     return binarySearch()
    

def main():
    solution = Solution()   
    nums = [4,5,6,7,0,1,2]
    target = 0
    out = solution.search(nums, target)
    print(out) 

if __name__ == "__main__":
    main()
