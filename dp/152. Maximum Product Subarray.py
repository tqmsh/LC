from typing import List 
class Solution:
    def maxProduct(self, nums: List[int]) -> int: 
        # f[i]: 以 i 结尾的连续乘基最最大
        # f2[i]: 以 i 结尾的连续乘基最最大
        
        # f[i] = max(a[i], f2[i - 1] * a[i]) if a[i] < 0 
        #      = max(a[i], f[i - 1] * a[i]) if a[i] >= 0
        # f2[i] = min(a[i], f[i] * a[i]) if a[i] < 0 
        #       = min(a[i], f2[i] * a[i]) if a[i] >= 0  
        # ans = max(ans, f[i]) 

        # f[0] = f2[0] = a[i]

        mx = nums[0]; mn = nums[0]; ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                mx, mn = mn, mx # 观察到，表达式差别就是当负时，f & f2 换着用
            mx = max(nums[i], mx * nums[i])
            mn = min(nums[i], mn * nums[i])
            ans = max(ans, mx)
        return ans
                    
def main():
    solution = Solution()  
    nums = [-1, 8, -1] 
    out = solution.maxProduct(nums)
    print(out) 

if __name__ == "__main__":
    main()
