from typing import List
from collections import Counter
from typing import Optional
from collections import defaultdict
import re

class Solution: 
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        path_w = []; path_l = 0; ans = []; # 字/字长; a(x) a a a / b(nx) b b b, path_w: [x, nx) 值
        
        # 边枚举边计算
        for w in words:
            if len(w) + path_l + len(path_w) > maxWidth:
                for i in range(maxWidth - path_l): path_w[i % (len(path_w) - 1 or 1)] += ' ' # 如想加入 3 空格，得在 0, 1, 2 处加入，即其 mod；满足优先左侧性质
                ans.append("".join(path_w))
                path_w = [w] # 维持对于下一个 w 的 [x, nx)
                path_l = len(w)
            else:
                path_w.append(w)
                path_l += len(w)
        return ans + [" ".join(path_w).ljust(maxWidth)]
                    
def main():
    solution = Solution()  
    words = ["This", "is", "an", "example", "of", "text", "justification."]; maxWidth = 16 
    out = solution.fullJustify(words, maxWidth)
    print(out) 

if __name__ == "__main__":
    main()
