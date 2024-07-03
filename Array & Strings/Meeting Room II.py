from typing import List
from collections import defaultdict

class Solution: 
    def minMeetingRooms(self, intervals: List[List[int]]) -> int: 
        # 离散化 + 差分
        b = defaultdict(int)  
        for interval in intervals:
            b[interval[0]] += 1
            b[interval[1] + 1] -= 1
        ans = -float('inf')
        sum = 0 
        # 枚举mp 模版 
        for k in sorted(b.keys()):   
            v = b[k]
            sum += v
            ans = max(ans, sum)
        return ans
    
def main():
    solution = Solution()
    intervals = [[0, 30], [5, 10], [15, 20]] 
    out = solution.minMeetingRooms(intervals)
    print(out) 

if __name__ == "__main__":
    main()