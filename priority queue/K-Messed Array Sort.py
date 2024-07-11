from typing import List 
from heapq import heappush, heappop 
class Solution: 
    def sort_k_messed_array(self, a, k):
        pq = []
        for i in range(k + 1): heappush(pq, a[i])
        j = k # j: pq 目前录了 [0, j]
        for i in range(len(a)):
            a[i] = heappop(pq)
            j += 1
            if j < len(a): heappush(pq, a[j])
        
# s_b[mx[0]:mx[1] + 1].decode()

    
def main():
    solution = Solution()
    
    arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]; k = 2 
    solution.sort_k_messed_array(arr, k)
    print(arr) 

if __name__ == "__main__":
    main()