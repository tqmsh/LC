from typing import List  
from collections import defaultdict
class Solution:
    def _find(self, x, f):
        if f[x] == x: return x 
        f[x] = self._find(f[x], f) 
        return f[x]
    
    def _merge(self, x, y, f): # 把 x 添到 y 下
        Fx = self._find(x, f)
        Fy = self._find(y, f)
        if Fx != Fy: f[Fx] = Fy 

    def longestConsecutive(self, nums: List[int]) -> int: 
        nums = set(nums)
        f = list(range(len(nums)))
        mp = {num: i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if num + 1 in mp: self._merge(i, mp[num + 1], f) 
            if num - 1 in mp: self._merge(i, mp[num - 1], f)
                
        cnt = [0] * len(nums); ans = 0 
        for i in range(len(nums)):
            fa = self._find(i, f)
            cnt[fa] += 1
            ans = max(ans, cnt[fa])
        return ans
    
def main(): 
    solution = Solution() 
    arr = [0,3,7,2,5,8,4,6,0,1]
    print(solution.longestConsecutive(arr))

if __name__ == "__main__":
    main()