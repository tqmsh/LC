from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        prev = [float('inf')] * n
        prev[src] = 0
        for _ in range(K + 1): 
            now = prev[:]  
            for u, v, w in flights:
                if prev[u] != float('inf'): now[v] = min(now[v], prev[u] + w)  
            prev = now 
        return prev[dst] if prev[dst] != float('inf') else -1  
    def findCheapestPrice(self, n, flights, src, dst, K):
        e = defaultdict(list)
        for u, v, w in flights: e[u].append((v, w))
            
        
        pq = [(0, src, 0)]  # (current cost, current node, stops so far)
        dist = [[float('inf')] * (K + 2) for _ in range(n)]  # (node, steps)
        dist[src][0] = 0 
        
        while pq:
            now_cost, now_pos, step = heappop(pq) 
            if now_pos == dst: return now_cost 
                
            if step > K:  continue   
            
            for v, w in e[now_pos]:
                nxt_cost = now_cost + w
                if nxt_cost < dist[v][step + 1]:
                    dist[v][step + 1] = nxt_cost
                    heappush(pq, (nxt_cost, v, step + 1))
        
        return -1 if min(dist[dst]) == float('inf') else min(dist[dst])

    
# Example usage:
sol = Solution()
n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
K = 1
print(sol.findCheapestPrice(n, flights, src, dst, K))  # Output should be 200

