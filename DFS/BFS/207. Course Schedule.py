# Question:
# Determine if you can finish all courses given the total number of courses and an array
# of prerequisite pairs, where each pair indicates a course and its prerequisite.

# Input:
# The input consists of an integer numCourses representing the total number of courses, 
# and a list of lists prerequisites, where each sublist contains two integers representing a 
# course and its prerequisite. This input specifies the course structure and dependencies.

# Output:
# The output is a boolean value, where true indicates that it is possible to finish all 
# courses, and false indicates that it is not possible due to circular dependencies or other 
# constraints. 

from typing import List 
from collections import deque

class Solution:
   
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inn = [0] * numCourses
        e = [[] for _ in range(numCourses)]
        
        for x in prerequisites:
            e[x[1]].append(x[0])
            inn[x[0]] += 1

        # 拓扑序 模版
        # bfs
        q = []
        for i in range(numCourses):
            if inn[i] == 0:
                q.append(i)
        
        vis = []
        while q:
            u = q.pop(0)
            vis += [u]
            for v in e[u]:
                inn[v] -= 1
                if inn[v] == 0:
                    q.append(v)
        
        # return numCourses == vis
    
        # dfs  

        vis = [0] * numCourses  

        # u 子树存不存在倒流
        def dfs(u):
            if vis[u] == 1: return False # 已查，树合法无环
            if vis[u] == -1: return True # 这个树倒流了，存在环
            vis[u] = -1 # 录
            for v in e[u]:
                if dfs(v): return True 
            vis[u] = 1
            return False
        for x in range(numCourses):
            if dfs(x):
                return 0
        return 1
def main(): 
    solution = Solution() 
    numCourses = 2
    prerequisites = [[1,0]]
   
    out = solution.canFinish(numCourses, prerequisites) 
    print(out) 

if __name__ == "__main__":
    main()