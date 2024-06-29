from typing import List  

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        ans = []
        intervals.sort(key = lambda x: (x[0], x[1]))  
        start = intwervals[0][0]; finish = intervals[0][1] 
        for i in range(1, len(intervals)): 
            if finish >= intervals[i][0]:
                finish = max(finish, intervals[i][1])
            else:
                ans.append([start, finish])
                start = intervals[i][0]
                finish = intervals[i][1]
        ans.append([start, finish]) 
        return ans
 

def main():
    solution = Solution()   
    intervals = [[1,4],[2,3]]
    out = solution.merge(intervals)
    print(out) 

if __name__ == "__main__":
    main()
