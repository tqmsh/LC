def hidden_password(s):
    # 贪心: 一步一步走，每一步都得最优
    # 找出 [idx, idx + len), 最优选择

    # 双指针，存在一个 idx, 可以把所有别的都打败
    i = 0; j = 1
    while i < len(s) and j < len(s): # O(n)

        # i, j 打擂台, 找到不一样的点，[i, i + k] != [j, j + k]
        k = 0
        while k < len(s) and s[(i + k) % len(s)] == s[(j + k) % len(s)]: k += 1

        # 如果所有 % len(s) 的可能性都没有成功，就会死循环，比如说 i, i + 1, i + ..., i + len(s) - 1, 都不重复，但是 i + len(s) % len(s) = i, 就死循环了
        if k == len(s): return i if i < j else j
        
        # i, j 打擂台，i 赢了, j 必然移动位置，[j, j + k) 已经比 [i, i + l) 小了，得往上移动
        if s[(i + k) % len(s)] > s[(j + k) % len(s)]: i = i + k + 1
        else: j = j + k + 1
        if i == j: j += 1  # 防止 i 和 j 重叠
    return i if i < j else j

print(hidden_password("dajlkfjad;fjidajlf"))