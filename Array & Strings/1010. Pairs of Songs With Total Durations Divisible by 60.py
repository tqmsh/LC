from typing import List
from collections import defaultdict
from math import comb
class Solution: 
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mp = defaultdict(int); ans1 = 0; cnt_0 = 0
        for x in time: 
            if not x % 60:
                cnt_0 += 1
                continue
            ans1 += mp[60 - x % 60]
            mp[x % 60] += 1
        return ans1 + comb(cnt_0, 2)

    
def main():
    solution = Solution() 
    time = [30,20,150,100,40] 
    out = solution.numPairsDivisibleBy60(time)
    print(out) 

if __name__ == "__main__":
    main()