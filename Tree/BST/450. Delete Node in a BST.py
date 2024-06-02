from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # f[i]: i子树，移除 k 后，长啥样
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 基
        if not root: return root
    
        # 状态转移
        if root.val > key:
            root.left = self.deleteNode(root.left, key)# R 不变，L 变
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key) 

        else:
            if root.right: # 把 R 子树最小值拿出来换位置 
                tmp = root.right  # 拿 R 子树 L 尾部地址 
                while tmp and tmp.left:  
                    tmp = tmp.left

                root.val = tmp.val # 如果是利用儿子结点信息计算，先递归再计算     
                root.right = self.deleteNode(root.right, tmp.val)  
            else:
                return root.left

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

def insertIntoBST(root: Optional[TreeNode], val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
 
def buildBST(values: List[int]) -> Optional[TreeNode]:
    root = None
    for value in values:
        root = insertIntoBST(root, value)
    return root

def main():
    values = [5,3,6,2,4,7]
    val = 0
    root = buildBST(values)
    solution = Solution()
    subtree = solution.deleteNode(root, val)
    print_bst(subtree)
if __name__ == "__main__":
    main()
