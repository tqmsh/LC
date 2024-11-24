import random
from typing import List 
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]: 
        ans_coords = [0] * 4; ans_sum = matrix[0][0]
        cur_r1 = 0; cur_c1 = 0; cur_r2 = 0; cur_c2 = 0

        for i1 in range(len(matrix)): # 枚举起始行
            psa = [0] * len(matrix[0])
            for i2 in range(i1, len(matrix)): # 枚举结束行
                # 最大子数组 模版
                mx = 0
                for j in range(len(matrix[0])): # 枚举列
                    psa[j] += matrix[i2][j] # psa[i2][j] = psa[i2 - 1][j] + matrix[i2][j]
                    # (1) 如果只需要维持 ans_sum
                    # mx = max(psa[j], mx + psa[j])
                    # ans_sum = max(mx, ans_sum)
                    # (2) 如果需要维持 ans_coords

                    # mx + psa[j] > psa[j]
                    if mx + psa[j] > psa[j]: mx += psa[j]
                    else:
                        mx = psa[j]
                        cur_r1 = i1 
                        cur_c1 = j
                    if mx > ans_sum: # 如果当前和比全局最大和大了
                        ans_sum = mx # 更新当前和为全局最大和
                        cur_r2, cur_c2 = i2, j # 更新一下行终点和列终点
                        ans_coords = cur_r1, cur_c1, cur_r2, cur_c2 # 更新结果
        return ans_coords
 