from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 0; l = 0
        for r in range(len(chars)):
            # vvvvv(v) x
            if r == len(chars) - 1 or chars[r] != chars[r + 1]:
                # a3b12c(j)ccccccc(i)d
                # [j, i] 
                cnt = r - l + 1
                # (1) log char
                chars[j] = chars[r]; j += 1
                l = r + 1
                if cnt == 1: continue
                # (2) log cnt
                for x in str(cnt):
                    chars[j] = x; j += 1
        return j

a = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

print(a[:Solution().compress(a)])
