from typing import List 
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def exist(self, rt, target):
        stk_s = []; stk_l = []
        small = 1; large = 1; ptr_s = rt; ptr_l = rt; path_s = -1; path_l = -1; 
        while 1: # 直到找到为止
            # 套 in 模版
            while small and (stk_s or ptr_s): 
                while ptr_s: # 模拟移至左边最深
                    stk_s += [ptr_s] #后进先出
                    ptr_s = ptr_s.left
                ptr_s = stk_s.pop()  
                path_s = ptr_s.val
                ptr_s = ptr_s.right
                small = 0
            while large and (stk_l or ptr_l): 
                while ptr_l: # 模拟移至左边最深
                    stk_l += [ptr_l] #后进先出
                    ptr_l = ptr_l.right
                ptr_l = stk_l.pop()  
                path_l = ptr_l.val
                ptr_l = ptr_l.right
                large = 0 
            if path_s != path_l and path_s + path_l == target: return 1
            elif path_s + path_l < target: small = 1 # 拿下一个 in order，即变大 
            elif path_s + path_l > target: large = 1 # 同理
            if path_s > path_l: return 0 # 重复了

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
    root = [5, 3, 7]
    print(Solution().exist(build_BT(root), 12)) 
if __name__ == "__main__":
    main()
