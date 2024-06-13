
from typing import List 
from collections import deque

class Solution: 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def dfs(current_idx, current_run, current_sum): 
            # 最优性剪枝， 如果不可能再优了，就没必要跑了
            # 可行性剪枝， 如果不存在方法，跑了也没意义，就不跑了

            if current_sum == target:
                combinations.append(current_run.copy())
                return 

            if current_idx >= len(candidates) or current_sum > target: 
                return
         
            for i in range(current_idx, len(candidates)):
                current_run.append(candidates[i])  
                dfs(i, current_run, current_sum + candidates[i])  
                current_run.pop() # backtrack 

        dfs(0, [], 0) 
        return combinations 
    
def main(): 
    solution = Solution() 
    candidates = [2,3,6,7]; target = 7  
    out = solution.combinationSum(candidates, target) 
    print(out) 

if __name__ == "__main__":
    main()