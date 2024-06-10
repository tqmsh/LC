
from typing import List 
from collections import deque

class Solution: 
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates) 
        combinations = []
        
        # dfs
        def dfs(current_idx, current_run, current_sum):   
            if current_sum == target:
                combinations.append(current_run.copy())
                return 

            if current_idx >= len(candidates) or current_sum > target: 
                return
         
            for i in range(current_idx + 1, len(candidates)):
                if i > current_idx + 1 and candidates[i] == candidates[i - 1]: continue
                current_run.append(candidates[i])  
                dfs(i, current_run, current_sum + candidates[i])  
                current_run.pop() # backtrack 

        dfs(-1, [], 0) 

        # bfs
        combinations = []
        queue = deque([(-1, [], 0)])  
        def bfs():
            while queue:
                current_idx, current_run, current_sum = queue.pop()
                if current_sum == target: 
                    combinations.append(current_run.copy())
                    continue  
                
                if current_idx >= len(candidates) or current_sum > target: 
                    continue
                
                for i in range(current_idx + 1, len(candidates)): 
                    if i > current_idx + 1 and candidates[i] == candidates[i - 1]: continue
                    queue.extend([(i, current_run + [candidates[i]], current_sum + candidates[i])]) 
        bfs()
        return combinations 
    
    
def main(): 
    solution = Solution() 
    candidates = [10,1,2,7,6,1,5]; target = 8 
   
    out = solution.combinationSum2(candidates, target) 
    print(out) 

if __name__ == "__main__":
    main()