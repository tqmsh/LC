# a = 20, b = 18, n = 2
# "2" ... "2" [:len - 18] = a * n - b = 20 * 2 - 18 = 22

# b = a * n_digits - ans_digits = 20 * len('2') - len('22')，由于唯一性，知道答案有了，L 就有了，然后 b 自然就出来了
 
from typing import List, Tuple

# 解决单个测试用例的问题
def find_ans(n: int) -> List[Tuple[int, int]]: 
    ans = []
    n_digits = len(str(n)) # 计算 n 的位数
    
    # 遍历所有可能的 a 值，范围是 1 到 10000
    for a in range(1, 10001):
        for ans_digits in range(1, min(a * n_digits, 6) + 1): # 枚举答案长度
            
            # 构造, 从必然入手, 构造 ans_digits 只有一种方法
            L = str(n)
            while len(L) < ans_digits: L += L  
            while len(L) > ans_digits: L = L[:-1]  
            L = int(L)
            
            # 枚举部分，直接算另一部分
            # 如果枚举了 a, ans_digits, 必然存在唯一的 L, 然后 b 也唯一化了， b = a * digit_n - ans_digits，如果 b 不这样的话，凑不出来

            b = a * n_digits - ans_digits
            if L == a * n - b and b >= 1: # 另一部分合法
                # 将符合条件的 (a, b) 对加入结果列表
                ans.append((a, b))
    
    return ans

# 示例测试用例
if __name__ == "__main__":
    # 示例输入
    test_n = [2, 3, 10]
    
    # 遍历每个输入 n，并打印符合条件的 (a, b) 对
    for n in test_n:
        pairs = find_ans(n)
        print(len(pairs))  # 输出符合条件的对的数量
        for a, b in pairs:
            print(a, b)  # 输出每对 (a, b)
