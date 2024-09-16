from typing import List
from collections import Counter

class Solution: 
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for x in tokens:
            if x == '+': stk.append(stk.pop() + stk.pop())
            elif x == '-':
                b = stk.pop(); a = stk.pop()
                stk.append(a - b)
            elif x == '*': stk.append(stk.pop() * stk.pop())
            elif x == '/': 
                b = stk.pop(); a = stk.pop()
                # int(a/b) -> 0, i.e. -2.333 -> -2
                # a//b -> -inf, i.e. -2.333 -> -3
                stk.append(int(a / b))
            else: stk.append(int(x))
        return stk[-1]
    
def main():
    solution = Solution()
    
    nums = [2,7,11,15]
    target = 9
    out = solution.twoSum(nums, target)
    print(out) 

if __name__ == "__main__":
    main()