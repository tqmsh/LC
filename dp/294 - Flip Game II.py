from functools import lru_cache
class Solution:
    @lru_cache(None)
    def _dp(self, now: str):
        if "++" not in now: return False
        return not all(
            self._dp(now[:i] + '--' + now[i + 2:])
            for i in range(len(now) - 1)
            if now[i:i + 2] == '++') 
    def canWin(self, s: str):
        return self._dp(s)
print(Solution().canWin("+"))