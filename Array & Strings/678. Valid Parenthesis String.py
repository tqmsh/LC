from typing import List

class Solution:  
    def checkValidString(self, s: str) -> str:
        mn = mx = 0
        for x in s:
            if x == '(': mn += 1; mx += 1 
            elif x == ')':  mn -= 1; mx -= 1 
            else: mn -= 1; mx += 1 # * = ) 或 * = ( 
                
            # 0 <= mn <= mx
            # 贪心：mn 可为 0 就为 0
            if mx < 0: return 0 
            mn = max(mn, 0) 
        return mn == 0
def main():
    solution = Solution()
    s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"


    out = solution.checkValidString(s)
    print(out) 

if __name__ == "__main__":
    main()