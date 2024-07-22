from typing import List 
from collections import deque

class Solution: 
    def _is_end(self, s):
        cnt = 0
        for c in s:
            if c == '(': cnt += 1
            elif c == ')': cnt -= 1
            if cnt < 0: return 0
        return cnt == 0
        
    def _bfs(self, s, ans):
        q = [s]; vis = set(); vis.add(s); f = 1
        while q:
            now = q.pop(0)
            if self._is_end(now):
                ans.append(now)
                f = 0
            if f:
                for i, c in enumerate(s):
                    if c not in "()": continue
                    nxt = now[:i] + now[i + 1:]
                    if nxt not in vis:
                        q.append(nxt)
                        vis.add(nxt)
        return -1

    def remove_invalid_parentheses(self, s: str) -> List[str]:
        ans = []
        self._bfs(s, ans) 
        return ans
         
def main(): 
    solution = Solution() 
    s = "()())()" 
    out = solution.remove_invalid_parentheses(s) 
    print(out) 

if __name__ == "__main__":
    main()