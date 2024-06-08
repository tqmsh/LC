# Question:
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths
# from node 0 to node n - 1 and return them in any order. The graph is given as follows: graph[i]
# is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to
# node graph[i][j]).

# Input:
# The input is a list of lists, where each list at index i contains the nodes that can be reached
# from node i. This input defines the edges and the structure of the directed acyclic graph.

# Output:
# The output is a list of lists, where each inner list represents a path from node 0 to node n - 1
# in the DAG, reflecting all possible paths from the source node to the target node.

from typing import List 
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = [] 
        # 走图 E[u] 模版
        def dfs(u, f, cur):   
            if u == len(graph) - 1: 
                ans.append(cur.copy())
                return  
            
            for v in graph[u]:
                if v  == f: continue
                dfs(v, u, cur + [v]) 

        dfs(0, -1, [0])    
        # bfs  
        q = deque([(0, -1, [0])])  
        def bfs():
            while q: 
                u, f, cur = q.popleft() 
                if u == len(graph) - 1: 
                    ans.append(cur)
                    continue   
                
                for v in graph[u]:
                    if v == f: continue
                    q.append((v, u, cur + [v])) 

        bfs()
        return ans
    
def main(): 
    solution = Solution() 
    graph = [[1,2],[3],[3],[]] 
    out = solution.allPathsSourceTarget(graph) 
    print(out) 

if __name__ == "__main__":
    main()