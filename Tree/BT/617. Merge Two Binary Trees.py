from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    # f[i]: 以t1=t2=i为根的子树，全处理好后，的结果
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 初始化
        if not t1: return t2 
        if not t2: return t1

        # 状态转移

        print(t1.val, t2.val)
        ans = TreeNode(t1.val + t2.val)
        ans.left = self.mergeTrees(t1.left, t2.left)
        ans.right = self.mergeTrees(t1.right, t2.right) 

        # f[i] = ans
        return ans

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
    solution = Solution()
    root1 = build_BT([1,3,2,5])
    root2 = build_BT([2,1,3,None,4,None,7])
    out = solution.mergeTrees(root1, root2) 
    print_bst(out)

if __name__ == "__main__":
    main()
