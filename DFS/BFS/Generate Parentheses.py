# Question:
# Generate all combinations of well-formed parentheses. A parenthesis combination is well-formed
# if each opening parenthesis "(" is closed by a matching closing parenthesis ")" in the correct order.

# Input:
# The input is an integer n representing the number of pairs of parentheses to generate combinations for.

# Output:
# The output is a list of strings, where each string represents a valid combination of parentheses with n pairs.
# Each combination should be well-formed, with all opening parentheses "(" closed by matching closing parentheses ")".

from typing import List 
from collections import deque

class Solution:   
    def _dfs(self, current_open_count, current_close_count, current_run, result, total_pairs):
        if current_open_count == current_close_count and current_open_count + current_close_count == 2 * total_pairs: 
            result.append(current_run)
            return
        # 能进门，必然合法，在这个基础上进行合法的扩散
                        # 添加 ( 永远合法，例如 ()(, 或者 (((
                        #，只要确保以后有办法用 ）给他补上，即 < n
        if current_open_count < total_pairs: self._dfs(current_open_count + 1, current_close_count, current_run + '(', result, total_pairs) 
        if current_close_count < current_open_count: self._dfs(current_open_count, current_close_count + 1, current_run + ')', result, total_pairs) 

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self._dfs(0, 0, "", result, n)
        return result
def main(): 
    solution = Solution() 
    n = 3 
    out = solution.generateParenthesis(n) 
    print(out) 

if __name__ == "__main__":
    main()