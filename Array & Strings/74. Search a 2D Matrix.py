from typing import List 
class Solution:  
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def b(matrix):  
            l, r = 0, len(matrix) * len(matrix[0]) - 1
            while l <= r:
                mid = (l + r) // 2
                # 数学
                # id = idx * rlen + idy
                midx, midy = mid // len(matrix[0]), mid % len(matrix[0]) 
                if matrix[midx][midy] == target:
                    return True
                elif matrix[midx][midy] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False 
        
        return b(matrix)
    

def main():
    solution = Solution()   
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    out = solution.searchMatrix(matrix, target)
    print(out) 

if __name__ == "__main__":
    main()
