from collections import defaultdict 
class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = [''] * len(s)
        mp = defaultdict(int)
        mx = -float('inf')
        for ch in s: 
            mp[ch] += 1
            mx = max(mx, mp[ch])
        # 看看最大值是否溢出/不合法，如果最大值都合法，剩下的必然合法，否则剩下的必然不合法
        if mx > (len(s) + 1) // 2: return ""

        i = 0 # 必然同样的字按照一空一的规律徘
        for k, v in mp.items():
            if k in ans: continue
            while v:
                if i >= len(s): i = 1
                ans[i] = k
                i += 2
                v -= 1

        return "".join(ans)
print(Solution().reorganizeString("aaaaaaaaaaaaaa;alsfklasjjfldajdf"))