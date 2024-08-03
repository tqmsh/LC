from typing import List 
from collections import defaultdict
import math
class Solution:
    def getLongestSubsequence(self, a: List[int], n: int) -> bool: 
        dp = [0] * (len(a)); dp[0] = 1 
        e =  [-1] * (len(a))
        for i in range(1, len(a)):
            for j in range(i):
                if 1 <= a[i] - a[j] <= n:  
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        e[i] = j

        i = dp.index(max(dp)); ans = [] 
        while i != -1:    
            ans.append(a[i])
            i = e[i]
        return ans[::-1]

def main():
    solution = Solution()  
    input = [1,4,2,7,8]
    out = solution.getLongestSubsequence(input, 3)
    print(out) 

if __name__ == "__main__":
    main()
