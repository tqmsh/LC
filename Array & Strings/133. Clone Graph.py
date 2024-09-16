from collections import defaultdict
from typing import Dict, Set, List

class Node:
    def __init__(self, val: int, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def _dfs(self, u: Node, vis: Set[Node], f: Dict[Node, Node]) -> None:
        vis.add(u)   
        f[u] = Node(u.val) # f[u]: u 子树，地址全换，重组结果

        for v in u.neighbors:
            if v in vis: continue 
            self._dfs(v, vis, f)   
            f[u].neighbors.append(f[v])

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        vis: Set[Node] = set()  # Visited set to track visited nodes
        f: Dict[Node, Node] = {}  # A map to store original-to-clone node mapping
        self._dfs(node, vis, f)  # Start DFS from the node
        return f[node]  # Return the cloned node

def build_graph(adjList: List[List[int]]) -> Node: 
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
        if n.val in visited: return 
        visited.add(n.val)
        for neighbor in n.neighbors:
            adj_list[n.val].append(neighbor.val)
            dfs(neighbor)

    dfs(node)
    return [adj_list[i] for i in range(1, len(adj_list) + 1)]

def main():
    solution = Solution() 
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]  # Input graph adjacency list
    original_node = build_graph(adjList)  # Build original graph
    out = solution.cloneGraph(original_node)  # Clone the graph
    print(display_adj_list(out))  # Display adjacency list of the cloned graph

if __name__ == "__main__":
    main()
