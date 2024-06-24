from typing import List 
from collections import defaultdict  
from itertools import accumulate
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        combines = [(aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]) for i in range(len(aliceValues))]
        combines.sort(reverse = True) # 从大到小排序, 按照这个选择导致的分差排序 
        
        alicePoints=sum([combine[1] for combine in combines[::2]])
        bobPoints=sum([combine[2] for combine in combines[1::2]]) 

        if alicePoints > bobPoints:
            return 1
        elif alicePoints < bobPoints:
            return -1
        return 0

def main():
    solution = Solution()  
    aliceValues = [2,4,3]; bobValues = [1,6,7]
    out = solution.stoneGameVI(aliceValues, bobValues)
    print(out)

if __name__ == "__main__":
    main()
