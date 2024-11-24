# 排序，按照右在右的顺序，这样就可以 a 左右扩散直到 把 b 删掉了

from typing import List, Tuple

def swipe_game(a: List[int], b: List[int]) -> Tuple[str, List[Tuple[str, int, int]]]:
    L = 0; idx = 0  # 初始化 L 和 idx
    a_idx_b_comp = []  # 存储 a 中匹配 b 的索引和 b 的连续段

    while L < len(b):
        # 找 b 联通快
        R = L
        while R + 1 < len(b) and b[L] == b[R + 1]: R += 1  # 修正条件以防止数组越界

        # 贪心，从必然入手，b 联通快处理，颜色和 在 a 中的出现顺序必然一样, 双指针
        while idx < len(a) and a[idx] != b[L]: idx += 1  # 寻找 a 中匹配 b[L] 的位置
        if idx == len(a): return "NO", []  # 如果找不到匹配的位置，返回 "NO"

        a_idx_b_comp.append((idx, L, R))
        idx += 1  # 一个 idx 只能对应一个 b_comp
        L = R + 1  # 更新 L，跳到下一个 b 的连续段起点

    ans = []
    # 贪心：排序，按照pos 右 -> 左，都杀右，这样确保必然 b 被实现
    for idx, L, R in reversed(a_idx_b_comp):
        if idx < R: ans.append(('R', idx, R))  # 添加右滑操作
    for idx, L, R in a_idx_b_comp:
        if L < idx: ans.append(('L', L, idx))  # 添加左滑操作

    return "YES", ans

if __name__ == "__main__":
    # 示例输入测试用例
    a = [1,2,4,3]
    b = [1,4,2,3]
    result, ops = swipe_game(a, b)
    print(result)
    if result == "YES":
        print(len(ops))
        for op in ops:
            print(f"{op[0]} {op[1]} {op[2]}")
