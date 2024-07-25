# Question:
# Given two strings, s and t, of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates) is included
# in the window. If there is no such substring, return an empty string.

# Input:
# The input consists of two strings: s, representing the main string where the search
# occurs, and t, representing the string containing the characters to be matched within
# the minimum window of s.

# Output:
# The output is the smallest substring of s that contains all characters from t. If no
# such substring exists, the output is an empty string.


from typing import List 
from collections import defaultdict 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = defaultdict(int)
        for ch in t: mp[ch] += 1
        mn = float('inf'); cnt = len(t); ans = 0; start = 0  
        j = 0
        for i in range(len(s)):
            while cnt > 0 and j < len(s): # 如果当下位置需要包含，将 j++，j会停在第一个不需要的地方
                if mp[s[j]] > 0: cnt -= 1
                mp[s[j]] -= 1
                j += 1
            if cnt == 0 and j - i < mn: 
                mn = j - i
                start = i

            mp[s[i]] += 1
            if mp[s[i]] > 0: cnt += 1
        return "" if mn == float('inf') else s[start:start + mn]


        # 对于任意一个字符不在 t 里，如果其被 j 包括时 mp -= 1, 那就会变负数，
        # 必然不会正的给 j cnt -= 1, 因为其被 j 负了，而 i 必然慢 j 一步，
        # i 必然不可能 mp += 1 吧其变正，从而 cnt += 1, 破坏 [i, j] 合法区间
        # while j < len(s):
        #     # 如果当下位置需要包含，将 j++，j会停在第一个不需要的地方
        #     if mp[s[j]] > 0: cnt -= 1 
        #     mp[s[j]] -= 1   
        #     j += 1    
        #     while cnt == 0: # [i， j) 合法 
        #         # 录最小   
        #         if j - i < mn: 
        #             mn = j - i
        #             ans = i 
        #         # i 右移一位，移至第一不合法
        #         mp[s[i]] += 1
        #         if mp[s[i]] > 0: 
        #             cnt += 1  
        #         i += 1   
        if mn == float('inf'):
            return ""
        return s[ans:ans + mn]

                    
def main():
    solution = Solution()  
    S = "abcdebdde"; T = "bde"
    out = solution.minWindow(S, T)
    print(out) 

if __name__ == "__main__":
    main()
