from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 双指针
        s, f = head, head
        for i in range(k - 1): # 再往前走 k - 1 步，连一开始的一步就是 k 步整
            if f: f = f.next

        # 走到头，停的时候f 没有后人了
        fir = f
        while f.next:
            f = f.next
            s = s.next

        sec = s
        fir.val, sec.val = sec.val, fir.val 
        return head
        

def main():
    # Convert array to linked list
    head = [1,2,3,4,5] 
    head = array_to_linked_list(head)
    k = 2  
    solution = Solution()   
    out = solution.swapNodes(head, k) 
    print_linked_list(out)

if __name__ == "__main__":
    main()
