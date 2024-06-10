
from typing import List 
from collections import deque
 
class Solution: 
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        
        def dfs(current_idx, current_run, current_sum):   
            if len(current_run) == k and current_sum == n:
                combinations.append(current_run.copy())
                return 

            if len(current_run) >= k or current_sum >= n: 
                return
         
            for i in range(current_idx, 10):  # Numbers from 1 to 9
                current_run.append(i)  
                dfs(i + 1, current_run, current_sum + i)  
                current_run.pop() # backtrack 

        # dfs(1, [], 0)  

        queue = deque([(1, [], 0)]) 
        def bfs():
            while queue:
                current_num, current_run, current_sum = queue.popleft()
                if len(current_run) == k and current_sum == n:
                    combinations.append(current_run)
                    continue
                
                if len(current_run) >= k or current_sum >= n:
                    continue
                
                for i in range(current_num, 10):  # Numbers from current_num to 9
                    queue.extend([(i + 1, current_run + [i], current_sum + i)])
                
        bfs()
        return combinations 
    
def main(): 
    solution = Solution() 
    k = 8; n = 44
   
    out = solution.combinationSum3(k, n) 
    print(out) 

if __name__ == "__main__":
    main()