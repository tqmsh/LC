from typing import List 

class Solution:
    def _get_rank(self, matrix, num):
        ans = 0 
        j = 0
        for i in range(len(matrix) - 1, -1, -1): 
            while j < len(matrix[0]) and matrix[i][j] <= num: # 移动到第一个不合法的位置，i.e. 1,2,3,4, x = 3, 
                                                              # 停在 4, 即 IDX = 3, 即 x = 3 的排名
                j += 1
            ans += j
        return ans 
    def _get_min_num(self, matrix, k): # O(n * log(MX-MN))
        l = matrix[0][0]
        r = matrix[-1][-1]
        ans = 0
        while l <= r:
            mid = (l + r) // 2  
            if self._get_rank(matrix, mid) >= k:
                ans = mid
                r = mid - 1
            else: 
                l = mid + 1
        return ans

    def kthSmallest(self, matrix, k):  
        return self._get_min_num(matrix, k)
                    
def main():
    solution = Solution()  
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    out = solution.kthSmallest(matrix, k)
    print(out) 

if __name__ == "__main__":
    main()
