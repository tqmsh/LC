from typing import List
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        avg, rem = divmod(sum(machines), len(machines))
        if rem: return -1
        path = 0; ans = float('-inf')
        for machine in machines:
            path += machine - avg
            ans = max(ans, max(abs(path), machine - avg))
        return ans

print(Solution().findMinMoves([0,0,11,5]))