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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 基
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        # 造bst，找中点
        s, f = head, head
        ls = s
        while f and f.next: # 走一遍链表 至至 vvvvvv(x) f -> f.n -> f.n.n，f 到头了，不能跑了，此时 s 就是中点
            ls = s
            s = s.next
            f = f.next.next
        node = TreeNode(s.val) 
        # 如果是利用儿子结点信息计算，先递归再计算   
        ls.next = None # ls -> s 这个断开
        node.left = self.sortedListToBST(head) # [head, mid] 造棵树
        node.right = self.sortedListToBST(s.next) # (s, mid] 造棵树

        return node

def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

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
    head = [-10, -3, 0, 5, 9]
    head = array_to_linked_list(head)
    bst_root = solution.sortedListToBST(head)
    print("BST Structure:")
    print_bst(bst_root)
if __name__ == "__main__":
    main()
