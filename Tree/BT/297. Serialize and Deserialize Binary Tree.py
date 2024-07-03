from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Codec: 
    def _to_string(self, root): # 每一个确保其处理位于最左侧的逗号
        if root is None: return "N," 
        return str(root.val) + "," + self._to_string(root.left) + self._to_string(root.right) # preorder: root, left, right
    
    def serialize(self, root): 
        return self._to_string(root)

    def _from_string(self, str):
        val = next(str) # preorder: root, left, right; 
                        # 把 iter 指针向右移一位，从上一个 val 移至这一个 val
        if val == "N": return None
        node = TreeNode(int(val))
        node.left = self._from_string(str)
        node.right = self._from_string(str)
        return node

    def deserialize(self, data): 
        return self._from_string(iter(data.split(",")))

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
def print_bst(node, level=0, label='.'):
    indent = '   ' * level
    if node is not None:
        print(f"{indent}-{label}: {node.val}")
        print_bst(node.left, level + 1, 'L')
        print_bst(node.right, level + 1, 'R')
    else:
        print(f"{indent}-{label}: None")
 
def main(): 
    tmp = Codec() 
    root = build_BT([1,2,3,None,None,4,5]) 
    str = tmp.serialize(root)
    print(str) 
    print_bst(tmp.deserialize(str))
if __name__ == "__main__":
    main()
