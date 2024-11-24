from typing import List

def getMaxMatrix(matrix: List[List[str]]) -> int: 
    ans = 0 

    for i1 in range(len(matrix)):  # 枚举起始行
        psa = [0] * len(matrix[0]) # 每次用 [i2 - 1] 的算 [i2]， i1 重构
        for i2 in range(i1, len(matrix)):  # 枚举结束行
            dp1 = 0 # 每一次用 [j - 1] 的算 [j], i2 重构
            dp2 = 0
            for j in range(len(matrix[0])):  # Enumerate column
                psa[j] += (matrix[i2][j] == 'X')  # psa[i1][i2][j] = psa[i1][i2 - 1][j] + (matrix[i2][j] == X)
                 
                # 先贪心算 dp2
                if matrix[i2][j] == 'X' or matrix[i1][j] == 'X': dp2 = 0  # dp2 Case (1)

                # psa[i1][i2][j] = 0, [i1, i2] 夹板中，j 列，没 X, 联通
                if not psa[j]:  
                    if not dp2:  dp2 = j  
                    dp1 = max(dp1, j - dp2 + 1) 
            ans = max(ans, dp1 * (i2 - i1 + 1))  # Update maximum area
    return ans

# Test the function with provided input
matrix = [
    list("......"),
    list("..X..X"),
    list("X..X.."),
    list("......"),
    list("..X...")
]

# Print the result
print(getMaxMatrix(matrix))
