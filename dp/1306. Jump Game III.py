
from typing import List 
from collections import deque

class Solution:
    def _check(self, arr, current_idx, vis):  
        if current_idx < 0 or current_idx >= len(arr): return 0  
        if current_idx in vis: return 0 
        return 1 
        
    def _dfs(self, arr, current_idx, vis):
        if current_idx not in vis: vis.add(current_idx) 
        nxt_idx = current_idx + arr[current_idx]
        if self._check(arr, nxt_idx, vis): self._dfs(arr, nxt_idx, vis)
        nxt_idx = current_idx - arr[current_idx]
        if self._check(arr, nxt_idx, vis): self._dfs(arr, nxt_idx, vis)

    def canReach(self, arr: List[int], start: int) -> bool:
        vis = set()  
        self._dfs(arr, start, vis)
        for i, num in enumerate(arr):
            if not num and i in vis: return 1
        return 0
    
def main(): 
    solution = Solution() 
    arr = [0,3,0,6,3,3,4]; start = 6
    out = solution.canReach(arr, start) 
    print(out) 

if __name__ == "__main__":
    main()