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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 头 - 1
        ans = ListNode(); ans.next = head; L = ans; x = head 
        while x:
            R = x.next
            # 边枚举边计算
            if x.val == val:
                # 用上一次的 L 做计算
                L.next = x.next

                # 这一次的 L 不变
            else:
                L = x

            x = R
        return ans.next




def main(): 
    solution = Solution()
    head = [1,2,2,1]
    val = 2
    head = array_to_linked_list(head) 
    print_linked_list(solution.removeElements(head, val))

if __name__ == "__main__":
    main()
