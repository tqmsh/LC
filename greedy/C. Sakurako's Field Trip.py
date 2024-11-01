class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 枚举，能用则用
        current_length = nums[0]
        for i in range(1, len(nums)):
            current_length -= 1
            if current_length < 0: return False
            current_length = max(current_length, nums[i])
        return True
