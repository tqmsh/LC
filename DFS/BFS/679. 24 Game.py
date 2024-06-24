
from typing import List  
import itertools

class Solution:
    def _comb(self, x, y):
        return [
            x+y,
            x-y,
            y-x,
            x*y,
            float('inf') if y==0 else (x / y),
            float('inf') if x==0 else (y/x)
        ]
    
    # remove 模版 
    def _remove(self, org, rmv): 
        for r in rmv:
            org.remove(r)
        return org
    
    def _dfs(self, current_run): 
        if len(current_run) == 1: 
            return abs(current_run[0]-24) < 0.001
        
        ok = 0
        for fir, sec in itertools.combinations(current_run, 2): 
            rest = self._remove(current_run[::],[fir, sec])
            for res in self._comb(fir, sec):
                ok |= self._dfs(rest + [res])
        return ok 

    def judgePoint24(self, cards: List[int]) -> bool:  
        return self._dfs(cards) 
    
def main(): 
    solution = Solution() 
    cards = [1,2,1,2]
    out = solution.judgePoint24(cards) 
    print(out) 

if __name__ == "__main__":
    main()