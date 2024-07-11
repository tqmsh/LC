from typing import List

class Solution:  
    def minSwaps(self, s: str) -> int:
        stk = []; ans = 0 
        for ch in s:
            # stk: 待匹配的合法符号
            if ch == '[':
                stk.append(ch)
            elif ch == ']':  
                if stk: 
                    stk.pop()
                else: # 处理删除/变合法
                    stk.append('[') # ) 必然变成 ( 才合法
                    ans += 1 
        return ans
def main():
    solution = Solution() 
    out = solution.minSwaps("]]][[[")
    print(out) 

if __name__ == "__main__":
    main()