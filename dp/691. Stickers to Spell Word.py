from typing import List 
from collections import defaultdict, Counter
from functools import lru_cache
import math
class Solution:
    @lru_cache(None)
    def _dp(self, now: str) -> int:
        if not now: return 0
        now_cnt = Counter(now)
        ans = float('inf')
        for sticker in self.stickers: # 枚举单词
            if now[0] in sticker: # 是否有用
                nxt = []
                for ch, freq in now_cnt.items(): # 枚举 现有的，删除被覆盖的
                    if freq > sticker.get(ch, 0): nxt.append(ch * (freq - sticker.get(ch, 0)))
                nxt = ''.join(nxt)
                ans = min(ans, self._dp(nxt) + 1)
        return ans  
    def minStickers(self, stickers: List[str], target: str) -> int:
        self.stickers =  [Counter(sticker) for sticker in stickers]
        ans = self._dp(target)
        return ans if ans != float('inf') else -1
    
def main():
    solution = Solution()  
    stickers = ["notice","possible"]; target = "basicbasic"
    out = solution.minStickers(stickers, target)
    print(out) 

if __name__ == "__main__":
    main()
