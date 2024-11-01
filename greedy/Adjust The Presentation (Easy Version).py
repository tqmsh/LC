from typing import List

def is_presentation_good(a: List[int], b: List[int]) -> str:
    pos_a = {a[i]: (i + 1) for i in range(len(a))}
    tot = 0
    mx = -1 # a 顺序用到何处了
    vis = set()
    for x in b:
        # 新来的
        if x not in vis: tot += 1 # b 内独特元素数量
        if x not in vis and pos_a[x] < mx: return 0 # （1）以前有调用a下表/演出顺序靠后的人出席，我被卡死了
        mx = max(mx, pos_a[x])
        vis.add(x)
        if tot != mx: return 0 # （2）没有陌生人占用出场顺序，挡在前面
    return 1
# Example Test Cases
def run_tests():
    # Test Case 1
    a1 = [1, 2, 3, 4]
    b1 = [1, 1]
    print(is_presentation_good(a1, b1))  # Expected: YA

    # Test Case 2
    a2 = [1, 2, 3]
    b2 = [1, 1, 2, 3, 3, 2]
    print(is_presentation_good(a2, b2))  # Expected: YA

    # Test Case 3
    a3 = [3, 1, 4, 2]
    b3 = [3, 1, 1, 2, 3, 4]
    print(is_presentation_good(a3, b3))  # Expected: TIDAK

run_tests()
