from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    xrent = head
    for value in arr[1:]:
        xrent.next = ListNode(value)
        xrent = xrent.next
    return head

def print_linked_list(head):
    xrent = head
    while xrent:
        print(xrent.val, end=" -> " if xrent.next else "\n")
        xrent = xrent.next

class Solution:
    def getKnodes(self, node, k):
        nodes = []
        while len(nodes) < k and node is not None:
            nodes.append(node)
            node = node.next
        return nodes

    # O(len(head) + m - n)
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if m == n: return head 
        ans = ListNode(0, next=head)
        L = ans 
        for _ in range(m - 1): L = L.next 
        nodes = self.getKnodes(L.next, n - m + 1) 
        
        # 调换 nodes 模版
        L.next = nodes[-1]
        nodes[0].next = nodes[-1].next
        for i in range(1, len(nodes)):
            nodes[i].next = nodes[i - 1]
        return ans.next
    # O(len(head)) 
    def reverseBetweenFast(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        ans = ListNode(0)
        ans.next = head
        L = ans 
        for _ in range(m - 1): L = L.next
            
        x = L.next
        for _ in range(n - m):
            R = x.next 
            x.next = R.next  
            R.next = L.next 
            L.next = R  
        return ans.next

def main():
    solution = Solution() 
    head = array_to_linked_list([1,2,3,4,5])
    head = solution.reverseBetweenFast(head, 2, 4) 
    print_linked_list(head)

if __name__ == "__main__":
    main()
