def solve(a):
    current_possible = [1] * len(a)
    # 边枚举边计算
    for i, val in enumerate(a): # 枚举一天
        current_possible[val] = 0
        # 每一个当下无法确定是否存在 Alibada 的地点，都有可能含有 Alibada, 
        # 然后它当下会左/右移动一次，这样一来，左/右边都变可能了, 然后本来的位置就变的不可能了
        # 为了好写，我们正难则反，不考虑哪些位置变的不可能了，直接挑选哪些变可能了
        next_possible = [0] * len(a)
        for i, x in enumerate(current_possible):
            if not x: # 造新的，这样的话，你造 nxt 的时候，不会把 cur 给改了
                next_possible[max(0, i - 1)] = 1
                next_possible[min(len(next_possible) - 1, i + 1)] = 1
        current_possible = next_possible
    return any(current_possible)
print(solve([0, 2, 4, 1, 3]))