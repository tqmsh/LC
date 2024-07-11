
from math import ceil
from collections import Counter

class Solution: 
    def _to_range(self, x):
        x += 26 * ceil((97 - x) / 26)
        return x
    def decrypt(self, word): 
        ans = ""
        pre = 1
        for i in range(len(word)):  
            num = self._to_range(ord(word[i]) - pre)
            ans += chr(num) 
            pre = ord(word[i])
        return "".join(ans) 
 
def main():
    solution = Solution()
    word = "dnotq" 
    out = solution.decrypt(word)
    print(out) 

if __name__ == "__main__":
    main()