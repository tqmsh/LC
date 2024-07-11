from typing import List 

class Solution: 
    def trap(self, height: List[int]) -> int: 
        # 双指针
        cur_i, cur_j = 0, len(height) - 1  
        cur_i_max = height[cur_i]; cur_j_max = height[cur_j] # i_max: [0, i] 最大值, j_max: [j, n] 最大值 
        ans = 0
        while cur_i < cur_j: # 考虑解决一节，我们可以用左/右极点较小的那一个算这一节所贡献的面积
            if cur_i_max < cur_j_max: # 选择解决 i 一节
                cur_i += 1 
                cur_i_max = max(cur_i_max, height[cur_i])
                ans += cur_i_max - height[cur_i] # 如果cur_i 再创新高，则不给予贡献
            else:
                cur_j -= 1 
                cur_j_max = max(cur_j_max, height[cur_j])
                ans += cur_j_max - height[cur_j]  
        return ans
                    
def main():
    solution = Solution()  
    height = [4,2,0,3,2,5]
    out = solution.trap(height)
    print(out) 

if __name__ == "__main__":
    main()
