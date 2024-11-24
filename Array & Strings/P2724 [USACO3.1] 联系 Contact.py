from functools import cmp_to_key
from collections import defaultdict
from typing import List, Dict
def cmp(a: Dict[str, int], b: Dict[str, int]):
    def f(x): return -1 if x else 1
    if a['f'] != b['f']: return f(a['f'] > b['f'])
    if a['len'] != b['len']: return f(a['len'] < b['len'])
    return f(a['val'] < b['val'])
def int_to_bin(n, l): return bin(n)[2:].zfill(l)
def find_frequent_sequences(A, B, n, s: str) -> List[str]:
    s = '0' + s; f_len_val = [] # 用来排序的数列，输出整体顺序
    for l in range(A, B + 1):
        val_to_f: defaultdict[int, int] = defaultdict(int)
        # 边枚举边计算 
        k = int(s[:l], 2)
        
        # Sliding Window
        for R in range(l, len(s)): 
            # [L, R] = len, R - L + 1 = len, L = R + 1 - len
            k = ((k << 1) & ((1 << l) - 1)) + int(s[R])
            # 0010 -> 0100; len = 4, (1 << len) - 1 = 10000 - 1 = 1111 

            val_to_f[k] += 1
        for k, v in val_to_f.items(): f_len_val.append({'f': v, 'len': l, 'val': k})
    f_len_val.sort(key = cmp_to_key(cmp))  

    ans = []; idx = 0; cnt_unique_f = 0 
    while cnt_unique_f < n and idx < len(f_len_val):
        # 频率一样的放一起
        f = f_len_val[idx]['f']; cnt_unique_f += 1; same_f = [] 
        while idx < len(f_len_val) and f_len_val[idx]['f'] == f: same_f.append(f_len_val[idx]); idx += 1

        ans.append(f"{f}")
        for L in range(0, len(same_f), 6):
            R = L + 6;                ans.append(' '.join(int_to_bin(x['val'], x['len']) for x in same_f[L: R]))
            # 出界会自动把剩下的带上                          # 把 val 转回二进制 背惦 0 x len  
    return ans

A = 2
B = 4
N = 10
s = "01010010010001000111101100001010011001111000010010011110010000000"
output = find_frequent_sequences(A, B, N, s) 
for line in output:
    print(line)
