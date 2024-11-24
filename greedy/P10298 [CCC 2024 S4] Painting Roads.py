from collections import defaultdict
from typing import List, Tuple

# 定义深度优先搜索（DFS）函数
def dfs(u, vis: set, e, dep, col):
    vis.add(u)  # 将当前节点标记为已访问
    for v, edge_idx in e[u]:
        if v in vis: continue  # 如果该邻接节点已经访问过，则跳过
        # 根据当前深度的奇偶性为边染色，奇偶性分类讨论
        if dep % 2 == 0: col[edge_idx] = 'R'  # 偶数深度染红色
        else: col[edge_idx] = 'B'  # 奇数深度染蓝色
        dfs(v, vis, e, dep + 1, col)  # 递归调用DFS，遍历下一个节点，并将深度加一
    # 不回溯，不同路径走到 u 一个结果

# 定义主函数并添加类型注解
def paint_roads(n: int, roads: List[Tuple[int, int]]) -> str:
    e = defaultdict(list)  # 用邻接表表示图
    for edge_idx, (u, v) in enumerate(roads): 
        e[u].append((v, edge_idx))  # 添加边到邻接表中
        e[v].append((u, edge_idx))  # 添加反向边，图是无向图
    vis = set()  # 创建集合用于存储访问过的节点
    col = ['G'] * len(roads)  # 初始化颜色数组为灰色

    # 遍历每个节点，确保每个连通分量都被访问
    for i in range(1, n + 1): 
        if i not in vis: dfs(i, vis, e, 0, col)  # 对未访问的节点调用DFS
    return ''.join(col)  # 返回染色方案作为字符串

# 测试案例
# 输入样例 #1 的测试用例
n = 5  # 节点数量
roads = [(1, 2), (2, 4), (5, 2), (4, 5), (4, 3), (1, 3), (1, 4)] 
print(paint_roads(n, roads))   