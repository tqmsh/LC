# Question:
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.

# Input:
# The input is a string of digits from 2 to 9, where each digit maps to a set of letters as on
# a telephone keypad. This input defines the digits whose corresponding letter combinations
# need to be found.

# Output:
# The output is a list of strings, where each string represents a possible letter combination
# that the input digits could represent, reflecting all possible combinations.

from typing import List 
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dict 模版 
        mp = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'] 
        }
        ans = [] 
        def dfs(id, cur):   
            if id >= len(digits):
                ans.append(cur)
                return 

            for x in mp[digits[id]]: 
                dfs(id + 1, cur + x) 

        if digits == "": return [] # 基无法转移  
        dfs(0, "")  

        # bfs
        ans = [] 

        q = deque()  
        def bfs():
            while q:
                id, cur= q.popleft()
                if id >= len(digits):
                    ans.append(cur)
                    continue
                
                for x in mp[digits[id]]:  
                    q.append((id + 1, cur + x)) # 维持下一个dfs在填的坑可选的信息 [id + 1, len)
                    
        if digits == "": return [] # 基无法转移  
        q.append((0, ""))   
        
        bfs()
        return ans 
    
def main(): 
    solution = Solution() 
    digits = "23"
   
    out = solution.letterCombinations(digits) 
    print(out) 

if __name__ == "__main__":
    main()