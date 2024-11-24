
from typing import List 
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        # dfs  
        inn = [0] * numCourses
        e = [[] for _ in range(numCourses)]
        
        for x in prerequisites:
            e[x[1]].append(x[0])
            inn[x[0]] += 1

        vis = [0] * numCourses  
        ans = []
        # u 子树存不存在倒流
        def dfs(u):
            if vis[u] == 1: return False # 已查，树合法无环
            if vis[u] == -1: return True # 这个树倒流了，存在环

            vis[u] = -1 # 录
            for v in e[u]:
                if dfs(v): return True 
            vis[u] = 1
            ans.append(u)
            return False
        for x in range(numCourses):
            if dfs(x):
                return []
        return reversed(ans)
def main(): 
    solution = Solution() 
    numCourses = 2
    prerequisites = [[1,0]]
   
    out = solution.canFinish(numCourses, prerequisites) 
    print(out) 

if __name__ == "__main__":
    main()