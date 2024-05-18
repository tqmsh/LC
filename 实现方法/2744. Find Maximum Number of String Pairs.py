from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # map 模版
        mp = {}  
        ans = 0
        for x in words:
            mp[x] = mp.get(x, 0) + 1
            mp[x[::-1]] = mp.get(x[::-1], 0) + 1
        for x in words:
            if (x[::-1] != x and mp.get(x[::-1], 0) > 1 ) or (x[::-1] == x and mp.get(x[::-1], 0) > 2): # 如果正/倒一样的话，会重数
                ans += 1
        return ans // 2   


    
def main():
    solution = Solution()
    
    words = ["ff","tx","qr","zw","wr","jr","zt","jk","sq","xx"] 
    out = solution.maximumNumberOfStringPairs(words)
    print(out) 

if __name__ == "__main__":
    main()