from collections import defaultdict
def modern_art_2(arr):
    s = defaultdict(lambda: -1); e = defaultdict(lambda: -1)
    # 维持联通快起点终点
    arr = [0] + arr + [0] 
    for i, col in enumerate(arr):
        if s[col] == -1: s[col] = i
        e[col] = i # 任何位置都有可能是终点
    
    #构建 类似于贪心思维，结合题目意思思考，怎么样才能更轻松的构造出结果 结论都是靠一步一步分析出来的，从小数据分析到大数据
    #贪心 按照位置，从左到右, 枚举能用则用，把能选的都选了; 按第一次出现顺序枚举的，占定维持还没结束的颜色

    # i.e. [0,1,4,5,1,3,3,0]
    # stk 变化 [0] | [0,1] | [0,1,4] [0,1] | [0,1,5] [0,1] | [0] | [0 3] | [0] | []
    # | 就是一个 Iteration 发生的事情

    stk = []; ans = 0
    
    for i, col in enumerate(arr):
        if i == s[col]: # 维持新的还没结束的颜色
            stk.append(col) 
            ans = max(ans, len(stk) - 1) # 0 不算一步
        
        # stk[-1] 的应涂区间中出现了别的颜色，同时这个颜色与 stk[-1] 不构成包含关系

        # i.e. 112(<- start)2222111 OK, 22222112(<-Not start)222211 BAD
        
        # 如果画布上出现了交错的颜色，必不合法
        if col != stk[-1]: return -1 
        if i == e[col]: stk.pop()
    return ans



# 测试用例
if __name__ == "__main__":
    # 示例测试
    print(modern_art_2([0,1,4,5,1,3,3]))