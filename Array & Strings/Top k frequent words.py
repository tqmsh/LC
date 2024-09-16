from typing import List
from collections import Counter
from heapq import heappush, heapreplace, heappop

class Solution: 
    def topKFrequent(self, words, k):
        # Step 1: Count the frequency of each word
        count = Counter(words)
        
        # Step 2: Use a min-heap to store the top k elements
        pq = []
        
        for word, freq in count.items():
            heappush(pq, (-freq, word))  # Push the negative frequency to simulate a max-heap
            if len(pq) > k:
                heappop(pq)
        
        # Step 3: Extract the elements from the heap and sort them by the frequency and lexicographical order
        result = []
        while pq:
            result.append(heappop(pq)[1])
        
        # Since we are using a min-heap, the order of elements will be reversed
        result.reverse()
        
        return result
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        pq = []
        for v, f in cnt.items(): heappush(pq, (-f, v))  
        ans = [heappop(pq)[1] for _ in range(k)]  
        return ans
    
    # k messed
    # k largest
    # find largest 
    
def main():
    solution = Solution()
    a = ['the', 'day', 'is', 'sunny', 'the', 'the', 'the', 'sunny', 'is', 'is']
    k = 4
    out = solution.topKFrequent(a, k)
    print(out) 

if __name__ == "__main__":
    main()

