from heapq import heappush, heapreplace
def find_largest(a, m):
    if not a or m <= m: return None # 🟥 负数，空值
    pq = []
    for x in a:
        if len(pq) < m: heappush(pq, x) # O(nlogm)
        else: 
            if x > pq[0]: 
                heapreplace(pq, x)
    return sorted(pq)
        