from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution: 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 离散化
        mp = {val: rank for rank, val in enumerate(inorder)}

        # 递归
        # f[i]: i 子树，按照 pre & in 规则
        def build(pre_left, pre_right, in_left, in_right):
            # 基
            if pre_left > pre_right: return None

            # 状态转移
            # f[i] = f[l] & f[r]
            root_val = preorder[pre_left]; root = TreeNode(root_val) 
            size_left = mp[root_val] - in_left
            root.left = build(pre_left + 1, pre_left + size_left, in_left, mp[root_val] - 1)
            root.right = build(pre_left + size_left + 1, pre_right, mp[root_val] + 1, in_right)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

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
    out = solution.buildTree([3,9,20,15,7], [9,3,15,20,7]) 
    print_bst(out)

if __name__ == "__main__":
    main()


# class Solution:
#     def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
#         stack = []
#         i = 0

#         while i < len(traversal):
#             # calculate the depth
#             depth = 0
#             while traversal[i] == '-':
#                 depth += 1
#                 i += 1

#             # calculate the value
#             value = ''
#             while i < len(traversal) and traversal[i] != '-':
#                 value += traversal[i]
#                 i += 1
#             value = int(value)

#             # create the node
#             curr_node = TreeNode(val = value)
            
#             # move to curr_level
#             while stack and len(stack) > depth:
#                 stack.pop()

#             # add
#             if stack:
#                 # left child
#                 if stack[-1].left is None:
#                     stack[-1].left = curr_node
#                 # right child
#                 else:
#                     stack[-1].right = curr_node
            
#             stack.append(curr_node)
#         return stack[0]