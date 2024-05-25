from typing import List 

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int: 
        # 思维题，负数形成楼梯形，可以走
        ans = 0
        # 双指针
        j = 0
        for i in range(len(grid) - 1, -1, -1): 
            while j < len(grid[0]) and grid[i][j] >= 0:
                j += 1
            ans += len(grid[0]) - j
        
        return ans 
                    
def main():
    solution = Solution()  
    grid = [[3,2],[1,0]]
    out = solution.countNegatives(grid)
    print(out) 

if __name__ == "__main__":
    main()
