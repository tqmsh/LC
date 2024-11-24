# 构建
# 类似于贪心思维，结合题目意思思考，怎么样才能更轻松的构造出结果, 在前面基础上多多少

def solve_b2(a):
    a = [0] + a
    if a[1] != 0: return 0 
    ans_coords = [0]
    ans_match = [0] 
    for j in range(1, len(a)): # 列必然不一样，用下标决定列 
        d = a[j]
        
        # 贪心：能和 0 Match 就和 0 Match

        # 枚举部分，直接算另一部分
        # d = |i_cur - i_1| + |j_cur - j_1|
        # d = i_cur - 1 + j_cur - 1
        # i_cur = d - j_cur + 2
        
        i = d - j + 2
        if 1 <= i: # 可以和 0 配对
            ans_coords.append((i, j))
            ans_match.append(1)
        else:  # 不能和 0 配对，那只能和其他一个同行
            # d = |i_cur - i_x| + |j_cur - j_x|, i_cur = i_x
            # d = 0             +  j_cur - j_x
            # j_x = j_cur - d
            j_x = j - d
            ans_coords.append((ans_coords[j_x][0], j))
            ans_match.append(j_x)
    return ans_coords[1:], ans_match[1:]

a = [0,1,3,1] 
print(solve_b2(a))