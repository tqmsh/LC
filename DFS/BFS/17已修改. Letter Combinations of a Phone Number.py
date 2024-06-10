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
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'] 
        }
        combinations = [] 
        def dfs(current_idx, current_combination):   
            if current_idx >= len(digits):
                combinations.append(current_combination)
                return 

            for letter in digit_to_letters[digits[current_idx]]: 
                dfs(current_idx + 1, current_combination + letter) 

        if digits == "": return [] # 基无法转移  
        dfs(0, "") # 出门处理 (0 的东西)

        # bfs
        combinations = [] 

        queue = deque([(0, "")])  
        def bfs():
            while queue:
                current_idx, current_combination = queue.pop() 
                if current_idx >= len(digits):
                    combinations.append(current_combination)
                    continue
                
                for letter in digit_to_letters[digits[current_idx]]: 
                    queue.extend([(current_idx + 1, current_combination + letter)])  
                    
        if digits == "": return [] # 基无法转移   
        bfs()
        return combinations 
    
def main(): 
    solution = Solution() 
    digits = "23"
   
    out = solution.letterCombinations(digits) 
    print(out) 

if __name__ == "__main__":
    main()