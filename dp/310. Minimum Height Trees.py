from typing import List 
from collections import defaultdict
import math
class Solution:
    def findMinHeightTrees(self, n: int, edge: List[List[int]]) -> List[int]:
        if n == 1: return [0] # 🟥 Edge Case
        inn = [0] * n
        e = defaultdict(list)
        for x in edge:
            u = x[0]; v = x[1] 
            e[u].append(v) 
            e[v].append(u)
            inn[v] += 1
            inn[u] += 1
        q = [x for x in range(len(inn)) if inn[x] == 1]  
        ans = []
        while q: 
            ans.clear()
            for _ in range(len(q)):
                u = q.pop(0); ans.append(u)
                for v in e[u]:
                    inn[v] -= 1
                    if inn[v] == 1: q.extend([v])
        return ans

        
def main():
    solution = Solution()  
    n = 4; edges = [[1,0],[1,2],[1,3]]
    out = solution.findMinHeightTrees(n, edges)
    print(out) 

if __name__ == "__main__":
    main()
