from typing import List

class Solution:  
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []; ans = ""
        # 边枚举边计算
        for ch in s:
            # 枚举包含的情况，正难则反，不考虑删除谁，只考虑添加谁
            if ch == '(':
                stk.append(ch)
                ans += ch
            elif ch == ')':
                if stk: 
                    stk.pop()
                    ans += ch
            else:
                ans += ch  
        ans = ans[::-1].replace('(', '', len(stk))[::-1] # 把结尾剩余的 ( 换掉
        return ans
def main():
    solution = Solution()
    
    s = "lee(t(c)o)de)"
    out = solution.minRemoveToMakeValid(s)
    print(out) 

if __name__ == "__main__":
    main()