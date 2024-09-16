from typing import List, Deque
from collections import deque

class Solution: 
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates) 
        combinations = []

        # Call dfs
        self._dfs(0, [], 0, candidates, target, combinations)

        # bfs
        combinations.clear()
        queue = deque([(0, [], 0)])  
        self._bfs(queue, candidates, target, combinations)
        
        return combinations 

    def _dfs(self, now_idx, prev_combination, prev_sum, candidates, target, combinations):   
        if prev_sum == target:
            combinations.append(prev_combination.copy())
            return 

        if now_idx >= len(candidates) or prev_sum > target: 
            return
     
        for i in range(now_idx, len(candidates)):
            if i > now_idx and candidates[i] == candidates[i - 1]:
                continue
            prev_combination.append(candidates[i])  
            self._dfs(i + 1, prev_combination, prev_sum + candidates[i], candidates, target, combinations)  
            prev_combination.pop() # backtrack 

    def _bfs(self, queue: Deque, candidates, target, combinations):
        while queue:
            now_idx, prev_combination, prev_sum = queue.pop()
            if prev_sum == target: 
                combinations.append(prev_combination.copy())
                continue  
            
            if now_idx >= len(candidates) or prev_sum > target: 
                continue
            
            for i in range(now_idx, len(candidates)): 
                if i > now_idx and candidates[i] == candidates[i - 1]:
                    continue
                queue.extend([(i + 1, prev_combination + [candidates[i]], prev_sum + candidates[i])])

    
def main(): 
    solution = Solution() 
    candidates = [10,1,2,7,6,1,5]; target = 8 
   
    out = solution.combinationSum2(candidates, target) 
    print(out) 

if __name__ == "__main__":
    main()