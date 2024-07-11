from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] 

class Solution: 
    # 环 dp 模版
    def cloneGraph(self, node: 'Node') -> 'Node':
        f = {}  
        # 输出 f[u]
        def dfs(u): 
            # DP 基; 转一圈回来了 
            if u in f: return f[u]
            
            # DP 状态转移
            f[u] = Node(u.val) # 救 -> 抄 
            for v in u.neighbors:  
                dfs(v)
                
                f[u].neighbors.append(dfs(v))
             
            return f[u]
        
        return dfs(node) if node else None #🟥不能用 f[node]，因为f[u] = Node(u.val) 的 u 的地址和进来的 node 的地址不一样
      

        
def build_graph(adjList): 
    # Create all nodes.
    nodes = [Node(i + 1) for i in range(len(adjList))]

    # Add neighbors.
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]

    return nodes[0]

def display_adj_list(node: 'Node'):
    if not node:
        return []

    adj_list = defaultdict(list)
    visited = set()

    def dfs(n: 'Node'):
        if n.val in visited:
            return
        visited.add(n.val)
        for neighbor in n.neighbors:
            print(adj_list[n.val])
            adj_list[n.val].append(neighbor.val)
            print(adj_list[n.val])
            dfs(neighbor)

    dfs(node)
    return [adj_list[i] for i in range(1, len(adj_list) + 1)]

def main():
    solution = Solution() 
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original_node = build_graph(adjList)
    out = solution.cloneGraph(original_node)
    print(display_adj_list(out)) 

if __name__ == "__main__":
    main()