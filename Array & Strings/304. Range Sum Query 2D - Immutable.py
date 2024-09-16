class NumMatrix:
    def __init__(self, matrix):
        n, m = len(matrix), len(matrix[0]) 
        # 1 index 2d arry 模版
        matrix = [[0] * (m + 1)] + [[0] + row for row in matrix]  
        self.sum = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.sum[i][j] = self.sum[i-1][j] + self.sum[i][j-1] - self.sum[i-1][j-1] + matrix[i][j]  
    
    def sumRegion(self, row1, col1, row2, col2):
        row1 += 1; col1 += 1; row2 += 1; col2 += 1
        # 2d psa 模版
        return self.sum[row2][col2] - self.sum[row2][col1 - 1] - self.sum[row1 - 1][col2] + self.sum[row1 - 1][col1 - 1]  
obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(obj.sumRegion(2, 1, 4, 3))