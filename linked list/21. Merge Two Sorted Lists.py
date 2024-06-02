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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:   
        ans = ListNode() 
        t = ans 
        while list1 and list2:   
            if list1.val < list2.val: 
                # 直接把整个 list 1 都加上去，但是没关系，因为t 会维持只用 list 1 头部的状态
                t.next = list1
                list1 = list1.next
            else:
                t.next = list2
                list2 = list2.next
            t = t.next 
        if list2:
            t.next = list2
        elif list1:
            t.next = list1 
        return ans.next
def main():
    solution = Solution()
    list1 = [1,2,4]
    list1 = array_to_linked_list(list1)
    list2 = [1,3,4] 
    list2 = array_to_linked_list(list2)

    head = solution.mergeTwoLists(list1, list2) 
    print_linked_list(head)

if __name__ == "__main__":
    main()
