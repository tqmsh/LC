from typing import List
from collections import Counter

class Solution:  
    def reverseWords(self, arr):
        # reversed 模版 
        arr[:] = reversed(arr[:]) 

        # 处理多余的空格
        i = 0
        while i < len(arr):
            # del 模版 
            if arr[i] == ' ' and (i == 0 or arr[i - 1] == ' '): del arr[i]
            else: i += 1
        while arr and arr[-1] == ' ': arr.pop()

        i = 0; j = 0
        while i < len(arr):
            while i < len(arr) and arr[i] == ' ': i += 1 # 把 i 移至字第一位
            j = i
            while j < len(arr) and arr[j] != ' ': j += 1 # 把 i 移至字最后一位过一位
            arr[i:j] = reversed(arr[i:j]) 
            i = j
        return arr
# s_b[mx[0]:mx[1] + 1].decode() 
def main():
    solution = Solution()
    arr = [ ' ', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', ' ',
        'm', 'a', 'k', 'e', 's', ' ',' ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
 
    out = solution.reverseWords(arr)
    print(out) 

if __name__ == "__main__":
    main()