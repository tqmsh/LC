from typing import List
def transform_permutation(a: List[int]):
    ans = []; even_has_n = 0; vis = set()

    # a[i] + ans[i] = n + 1, ans[i] = n + 1 - a[i]
    for i, x in enumerate(a):  
        ans.append(len(a) + 1 - x)
        if i % 2 == 0 and ans[-1] == len(a): even_has_n = 1
      
    # a =   1 2 3 4
    # ans = 4 3 2 1
    # sum = 5 5 5 5 

    # 构建， 类似于贪心思维，结合题目意思思考，怎么样才能更轻松的构造出结果 所有偶/奇数位置加一，奇/偶数位置不变，显然这是我们最多只能有这么多局部最大值
    for i in range(even_has_n, len(a), 2):
        ans[i] += 1; vis.add(ans[i]) 
 
    # a =   1 2 3 4
    # ans = 4 4 2 2
    # sum = 5 6 5 6 

    # 贪心，排序，按照位置，从左到右，按照值，从小到大，枚举能用则用；偶位置加一, 空出一个候补，可能占了一个基数位置，对于所有被影响的奇数答案，最小的被影响的和最小候补换，第二小被影响的和第二小空出来的换，以此类推，尽量维持最优规律
    ans_effected = [] 
    for i in range(1 - even_has_n, len(ans), 2): # O(n/2 log(n/2))
        ans_effected.append((ans[i], i))
    ans_effected.sort()
    
    
    # 双指针，随着 val 增加，替补 candidate 也增加
    mn_candidate = 1
    for val, idx in ans_effected:
        if val in vis: # 位置被占了, 得替补
            while mn_candidate in vis: mn_candidate += 1 # 双指针拿最小候补
            ans[idx] = mn_candidate
            vis.add(mn_candidate)
        else: vis.add(val) # 不用替补，占位置
            
    #                      如果不排序，尽量维持最优规律，缓冲偶数位带来的影响的话，就会这样
    # a =   1 2 3 4        1 2 3 4
    # ans = 3 4 1 2        1 4 3 2 
    # sum = 4 6 4 6        1 6 6 6，没了
    return ans

# 测试示例
# 示例 1：输入 n = 4，a = [4, 3, 2, 1]
print(transform_permutation([1, 2, 4, 5, 7, 6, 8, 3]))  # 应输出一个排列 