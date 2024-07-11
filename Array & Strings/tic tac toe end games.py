from typing import List  
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        move_to_val = {'X': 1, 'O': -1, ' ': 0}
        a = [move_to_val[move] for move in ''.join(board)]
        tot = sum(a)  # flatten ["XOX"," X ","   "] --> [1,-1,1,0,1,0,0,0,0]  
        if tot >> 1:  return 0  # 10 (binary) = 2 -> 1; or >= 2 
        # 如果最后走的是 X, 而 O 在这以前已经赢了，则不合法
        illegal = -3 if tot else 3
        if illegal in { a[0] + a[1] + a[2], a[3] + a[4] + a[5], a[6] + a[7] + a[8],
            a[0] + a[3] + a[6], a[1] + a[4] + a[7], a[2] + a[5] + a[8],
            a[0] + a[4] + a[8], a[2] + a[4] + a[6] }:  return 0 
        return 1


    
def main():
    solution = Solution()
    board = ["XOX","O O","XOX"]
    out = solution.validTicTacToe(board)
    print(out) 

if __name__ == "__main__":
    main()