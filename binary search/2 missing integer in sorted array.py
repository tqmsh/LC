from typing import List 
class Solution:
    def _bs(self, l: int, r: int, ans: set[int], a: List[int]):
        # 最坏 O(n) 但是 Early stopping 能帮忙
        if l > r or len(ans) == 2:  return
        mid = (l + r) // 2
        if mid + 1 < len(a) and a[mid + 1] - a[mid] > 1: ans.add(a[mid] + 1)
        if mid - 1 >= 0 and a[mid] - a[mid - 1] > 1: ans.add(a[mid] - 1)
        if len(ans) == 2: return
        self._bs(l, mid - 1, ans, a)
        if len(ans) == 2: return
            
        self._bs(mid + 1, r, ans, a)
    def find_missing(self, a: List[int], n: int) -> List[int]:
        if not a:return []
        ans = set()
        if a[0] != 1: ans.add(1)
        if a[-1] != n: ans.add(n)
        self._bs(0, len(a) - 1, ans, a)
        return list(ans)


sequence = '11222333566779'; int_list = [int(char) for char in sequence]
print(Solution().find_missing(int_list, 9))