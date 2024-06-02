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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        L = None
        x = head
        while x:
            R = x.next
            # 边枚举边计算, 巧妙的利用上一次结果快速计算当前结果
            x.next = L
            # 上一次计算结果
            L = x 
            x = R

        # x 到头了，拿 L 做答案
        return L

def main():
    solution = Solution()
    head = [-10, -3, 0, 5, 9]
    head = array_to_linked_list(head)
    head = solution.reverseList(head) 
    print_linked_list(head)

if __name__ == "__main__":
    main()
