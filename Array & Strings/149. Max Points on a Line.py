from typing import List
from collections import Counter, defaultdict

class Solution: 
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            cnt = defaultdict(int)
            cnt2 = 0
            for j in range(i + 1, len(points)): # 带 [0, j) 的情况已经前面枚举过了，没必要 
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2: 
                    cnt2 += 1
                    continue 
                dy = y2 - y1; dx = x2 - x1
                cnt[dy / dx] += 1  
            ans = max(ans, max(cnt.values()) + 1 if cnt else 1, (cnt2 + 1 if cnt2 else 0)) 
        return ans 
    
def main():
    solution = Solution()
    
    points = [[0,1],[0,0]]
    out = solution.maxPoints(points)
    print(out) 

if __name__ == "__main__":
    main()