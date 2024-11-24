from typing import List
def minimize_disturbance(a: List[int]) -> int:  
    for i in range(1, len(a) // 2):
        # XXX(i)XXXXXXX(len - i - 1)X(len - i)X
        before = (a[i] == a[i - 1]) + (a[len(a) - i - 1] == a[len(a) - i])
        after = (a[len(a) - i - 1] == a[i - 1]) + (a[i] == a[len(a) - i]) 
        # 贪心, 枚举能用则用
        if after < before: a[i], a[len(a) - i - 1]  = a[len(a) - i - 1], a[i] 
    return sum((a[i] == a[i - 1]) for i in range(1, len(a)))
      
print(minimize_disturbance([2, 1, 2, 3]))  # Expected output: 0
print(minimize_disturbance([1, 2, 2, 1, 2, 1]))  # Expected output: 1
print(minimize_disturbance([4, 5, 5, 1, 5]))  # Expected output: 1
print(minimize_disturbance([1, 4, 3, 5, 1, 1, 3]))  # Expected output: 0
print(minimize_disturbance([3, 1, 3, 2, 2, 3, 3]))  # Expected output: 2