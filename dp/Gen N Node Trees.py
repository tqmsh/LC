from typing import List 
from typing import Optional 
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp: defaultdict[int, list] = defaultdict(list)
        dp[1] = [TreeNode()]
        for i in range(3, n + 1, 2): # 基数不可能合法
            for j in range(1, i - 1, 2): # 枚举左边有多少个，最少 1， 最大 i
                # k + j + 1 = i, k = i - j - 1
                # k >= 1, i - j - 1 >= 1, i - j >= 2, j <= i - 2
                for l in dp[j]:
                    for r in dp[i - j - 1]:
                        dp[i].append(TreeNode(0, l, r))
        return dp[n]

def print_bst(node, level=0, label='.'):
    indent = '   ' * level
    if node is not None:
        print(f"{indent}-{label}: {node.val}")
        print_bst(node.left, level + 1, 'L')
        print_bst(node.right, level + 1, 'R')
    else:
        print(f"{indent}-{label}: None")

def main():
    solution = Solution()
    out = solution.allPossibleFBT(5) 
    print(out)
if __name__ == "__main__":
    main()
