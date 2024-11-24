from bisect import bisect_left
from typing import List 
from collections import defaultdict, deque
from queue import PriorityQueue
def _get_e_inn(observations, mid):
    e = defaultdict(list)
    inn = defaultdict(int)
    for i in range(mid + 1):
        for j in range(len(observations[i]) - 1):
            e[observations[i][j]].append(observations[i][j + 1])
            inn[observations[i][j + 1]] += 1
    return e, inn

# 判环 模版
def _no_cycle(inn, e, n): # O(m)
    q = deque()
    for i in range(1, n + 1):
        if not inn[i]: q.append(i) 
    cnt = 0
    while q:
        u = q.popleft(); cnt += 1
        for v in e[u]:
            inn[v] -= 1
            if not inn[v]: q.append(v)  
    return cnt == n

def check(mid, observations, n):
    e, inn = _get_e_inn(observations, mid) 
    if _no_cycle(inn, e, n): return 1
    return 0

def _top_sort_greedy(observations, mx_x, n, ans: List[int]):
    e, inn = _get_e_inn(observations, mx_x) 
    pq = PriorityQueue() # O(nlogm)
    for i in range(1, n + 1):
        if not inn[i]: pq.put(i) 
    while not pq.empty():
        u = pq.get(); ans.append(u)
        for v in e[u]:
            inn[v] -= 1
            if not inn[v]: pq.put(v)   

def solve(n, observations: List[List[int]]): 
    # 二分，最大化最小值

    # 最大化最小值 模版
    mx_x = bisect_left(range(len(observations)), 1, key = lambda x: not check(x, observations, n)) - 1 # vvvvvvvvv(v)xxxxxxxxxx O(logm)
    ans = []
    _top_sort_greedy(observations, mx_x, n, ans)
    return ans 
# 测试用例 1: 无环，合法观测，包含多个不连通的子图
observations1 = [
    [1, 2, 3],
    [4, 5, 6],
    [6, 7, 5]
]
n1 = 7  # 节点数量
print(solve(n1, observations1))  # 输出: True
