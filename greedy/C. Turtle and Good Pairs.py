from collections import Counter
def maximize_good_pairs(s: str) -> str:
    f = Counter(s); ans = ""
    for _ in range(len(s)): # 凑 s 个单词
        for c in sorted(f): # 有顺序扫一遍 mp, 能多去重就多去重
            if f[c]: ans += c; f[c] -= 1
    return ans
print(maximize_good_pairs("turtle"))