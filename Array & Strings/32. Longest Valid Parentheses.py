from typing import List

class Solution:  
    def longestValidParentheses(self, s: str) -> int:
        stk = [-1]  # Initialize stack with -1 to handle edge cases
        max_len = 0
        
        for i, ch in enumerate(s):
            # 枚举包含的情况，正难则反，不考虑删除谁，只考虑添加谁
            if ch == '(':
                stk.append(i)
            elif ch == ')':
                if stk:
                    stk.pop()
                    if stk:
                        max_len = max(max_len, i - stk[-1])
                    else:
                        stk.append(i)
        
        return max_len


class Solution: 
    def _solve(self, s):
        stk = []; 
        ans = 0
        path = ""
        # 边枚举边计算
        for ch in s:
            # 枚举包含的情况，正难则反，不考虑删除谁，只考虑添加谁
            if ch == '(':
                stk.append(ch)
                path += ch
            elif ch == ')':
                if stk: 
                    stk.pop()
                    path += ch
                    if not stk: ans = max(ans, len(path))
                else:
                    ans = max(ans, len(path)) 
                    path = ""
                    stk = []
        if not stk: ans = max(ans, len(path))
        return ans
    def longestValidParentheses(self, s: str) -> str:
        rev = s[::-1]
        ans = ""
        for i in range(len(rev)):
            if rev[i] == '(': ans += ')'
            else: ans += '('
        return max(self._solve(s), self._solve(ans))
       
def main():
    solution = Solution()
    s = "()(()"
    out = solution.longestValidParentheses(s)
    print(out) 

if __name__ == "__main__":
    main()