from typing import List, Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def _dfs(self, u: TreeNode, f: TreeNode, sum: defaultdict):
        if not u: return 
        sum[u] = u.val # 子树权值和
        self._dfs(u.right, u, sum)
        sum[u] += sum[u.right] # 如果是利用儿子结点信息计算，先递归再计算  
        u.val += sum[u.right]
        if u == f.left: u.val += f.val
        self._dfs(u.left, u, sum)
        sum[u] += sum[u.left]
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum = defaultdict(int)
        self._dfs(root, TreeNode(), sum)
        return root

# BST 模版
def print_bst(node, level=0, label='.'):
    indent = '   ' * level
    if node is not None:
        print(f"{indent}-{label}: {node.val}")
        print_bst(node.left, level + 1, 'L')
        print_bst(node.right, level + 1, 'R')
    else:
        print(f"{indent}-{label}: None") 

def build_BT(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        current = queue.pop(0)
        if arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    return root
def main():
    root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    root = build_BT(root)
    solution = Solution()
    subtree = solution.convertBST(root)
    print_bst(subtree)
if __name__ == "__main__":
    main()
