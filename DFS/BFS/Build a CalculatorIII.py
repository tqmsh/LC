from typing import List 
from collections import deque

class Solution:
    def _get_j(self, s, i):
        lvl = 0
        for id in range(i, len(s)):
            if s[id] == '(': lvl += 1
            elif s[id] == ')': lvl -= 1
            if lvl == 0: return id
        return 0 
    def calculate(self, s):
        stk = []
        cur_num = 0; cur_opt = '+'; i = 0 
        while i < len(s):  
            # (1)造目前的数字 
            if s[i].isdigit(): cur_num = cur_num * 10 + int(s[i])  
            elif s[i] == '(':
                j = self._get_j(s, i)
                cur_num = self.calculate(s[i + 1: j])
                i = j # i 后面会自己增1的
            # (2)到符号，数字结束，入盏/融合 
            if s[i] in "+-*/" or i == len(s) - 1: 
                if cur_opt == '+': stk.append(cur_num)
                if cur_opt == '-': stk.append(-cur_num)
                if cur_opt == '*': stk[-1] *= cur_num
                if cur_opt == '/': stk[-1] //= cur_num  
                cur_opt = s[i]; cur_num = 0 
            i += 1
        return sum(stk)
def main(): 

    solution = Solution() 
    input = "2*(5+5*2)/3+(6/2+8)"  
    out = solution.calculate(input) 
    print(out) 

if __name__ == "__main__":
    main()