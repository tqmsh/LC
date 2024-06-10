import collections
from typing import List

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False
 
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        curr = self.root
        for i in range(len(path)):
            curr = curr.children[path[i]]
        curr.end = True

    def search(self, path):
        curr = self.root
        for i in range(len(path)):
            curr = curr.children[path[i]]
            if curr.end and i != len(path) - 1:
                return False
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()  
        ans = []
        for word in words:
            trie.insert(word)

        ans = []; vis = set()  
        def check(x, y): 
            # 没有越界，没有走过，不是障碍 (这一点以后特判)
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]): return 0  
            if (x, y) in vis: return 0 
            return 1 
        
        def dfs(x, y, f, path): # x, y, 父亲是 f，至此走的路
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
            u = f.children[board[x][y]] # x, y 是哪一颗

            if u.end:
                ans.append(path)
                u.end = 0 # 防重复发育

            vis.add((x, y))  
            for dx, dy in directions:
                nx, ny = x + dx, y + dy 
                if check(nx, ny) and board[nx][ny] in u.children:
                    dfs(nx, ny, u, path + board[nx][ny])
            vis.remove((x, y))

            # 如果这个是叶子，把他删了
            if not u.children: 
                f.children.pop(board[x][y])

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] in trie.root.children:
                    dfs(x, y, trie.root, board[x][y])

        return ans
def display_grid(array):
    for row in array:
        for element in row:
            print(f"{element}\t", end="")
        print()  # Newline after each row
    print('--------------------------------------------------------') 
def main(): 
    solution = Solution() 
    board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]; words = ["oa","oaa"]
    display_grid(board)
    out = solution.findWords(board, words) 
    print(out)

if __name__ == "__main__":
    main()
