from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
import re

class Solution: 
    def find_duplicates(self, arr1, arr2):
        i, j = 0, 0
        ans = []
        while i < len(arr1) and j < len(arr2):  
            if arr1[i] == arr2[j]: 
                ans.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]: i += 1
            else: j += 1
        return ans
                    
def main():
    solution = Solution()  
    arr1 = [1, 2, 3, 5, 6, 7]; arr2 = [3, 6, 7, 8, 20]

    out = solution.find_duplicates(arr1, arr2)
    print(out) 

if __name__ == "__main__":
    main()
