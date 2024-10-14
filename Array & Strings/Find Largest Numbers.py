from heapq import heappush, heapreplace
def find_largest_m_elements_reverse_sorted(lists, M):
    pq = []

    for lst in lists:
        for num in lst[:M]:   
            if len(pq) < M:
                heappush(pq, num)
            else:
                if num > pq[0]: heapreplace(pq, num)
                    
     
    return sorted(pq)

lists = [
    [9, 5, 1],
    [8, 6, 2]
    [10, 7, 3]
]
M = 4
result = find_largest_m_elements_reverse_sorted(lists, M)
print(result)  # Expected output: [7, 8, 9, 10]