from typing import List, Tuple
from collections import defaultdict
from math import ceil, floor

class Solution: 
    def _rt_set(self, cnt_leaf, s: str):
        # 和根不一样 = 给分          MAX先手能用一半回合向上取整叶子?
        if s[1] == '0': return cnt_leaf['1'] + ceil(cnt_leaf['?'] / 2)
        return cnt_leaf['0'] + ceil(cnt_leaf['?'] / 2)

    def calculate_score(self, n: int, edges: List[Tuple[int, int]], s: str) -> int:
        inn = defaultdict(int); cnt_leaf = defaultdict(int); s = " " + s          
        for u, v in edges: inn[u] += 1; inn[v] += 1 # 枚举叶子
        for i in range(2, n + 1):  # 枚举叶子
            if inn[i] == 1: cnt_leaf[s[i]] += 1  # If the degree is 1, it's a leaf node
        
        # If the root is not '?', calculate the score directly
        if s[1] != '?': return self._rt_set(cnt_leaf, s)
        
        # When cnt_leaf['0'] and cnt_leaf['1'] are not equal
        if cnt_leaf['0'] != cnt_leaf['1']:
            # MAX先把RT换成和频繁者不一样的，拿所有现成分，转后手用一半回合向下取整叶子?
            return max(cnt_leaf['0'], cnt_leaf['1']) + floor(cnt_leaf['?'] / 2)
        
        cnt_mid = s.count('?') - 1 - cnt_leaf['?']
        # 先填根的人必然会亏，所以此时先填非根非叶子节点，考虑其问号个数的奇偶性即可。需要考虑多余的？能让先手交换先后手
        if cnt_mid % 2 != 0:  # 有多余 ?, 先手交换成后手，无论MIN做什么，MAX都能做一对Leaf? != Rt?, 这样下来的话就成了_rt_set，但是因为这个操作，答案 + 1
            cnt_leaf['?'] -= 1
            # WLOG rt = 1 (没关系，因为都一样多)
            s = s[:1] + '1' + s[2:]  # Change root to '1'
            return self._rt_set(cnt_leaf, s) + 1
        
        # MIN 填了最后一个 MID ?, MAX 填任何值，MIN 可以凑成一对Leaf? == Rt? 这样下来的话就成了_rt_set 
        cnt_leaf['?'] -= 1
        s = s[:1] + '1' + s[2:]  # Change root to '1'
        return self._rt_set(cnt_leaf, s)
    
n1 = 4
edges1 = [(1, 2), (1, 3), (4, 1)]
s1 = "0101"
print(Solution().calculate_score(n1, edges1, s1))  # Expected output: 2

n2 = 4
edges2 = [(1, 2), (3, 2), (2, 4)]
s2 = "???0"
print(Solution().calculate_score(n2, edges2, s2))  # Expected output: 1

n3 = 5
edges3 = [(1, 2), (1, 3), (2, 4), (2, 5)]
s3 = "?1?01"
print(Solution().calculate_score(n3, edges3, s3))  # Expected output: 1