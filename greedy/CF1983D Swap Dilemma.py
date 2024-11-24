from typing import List
def can_make_equal(a: List[int], b: List[int]) -> str:
    
    # 构建, 类似于贪心思维，结合题目意思思考，怎么样才能更轻松的构造出结果, 结论都是靠一步一步分析出来的，从小数据分析到大数据 

    # 如何轻松构建？

    # 贪心：从必然入手 把当前的逐步, 用最优法，变成必然，把 a 当必然，让 b 变成 a; 用 a 的 两个数字一直换换换, 然后 swap a[i], b[j] 等价于 a 那两个 数字 换 2 * (j - i) - 1 次
    cnt_swaps = 0
    for i in range(len(a)): 
        if a[i] != b[i]: # 必然换 
            for j in range(i + 1, len(b)):
                if b[j] == a[i]:
                    b[i], b[j] = b[j], b[i]
                    cnt_swaps += 2 * (j - i) - 1; cnt_swaps %= 2
                    break # Early Stopping 防 O(n^2) 爆掉
        if a[i] != b[i]: return 'NO'
    return 'YES' if not cnt_swaps else 'NO'
    

        
 
# 测试用例
if __name__ == "__main__":
    # 示例测试用例
    print(can_make_equal([1, 2, 3, 4], [1, 2, 3, 4]))  # 应输出 "YES"
    print(can_make_equal([1, 3, 4, 2, 5], [7, 1, 2, 5, 4]))  # 应输出 "NO"
    print(can_make_equal([1, 2, 3, 4], [4, 3, 2, 1]))  # 应输出 "YES"
    print(can_make_equal([1, 2, 3], [1, 3, 2]))  # 应输出 "NO"
    print(can_make_equal([1, 5, 7, 1000, 4], [4, 1, 7, 5, 1000]))  # 应输出 "NO"
    print(can_make_equal([1, 4, 2], [1, 3, 2]))  # 应输出 "NO"
