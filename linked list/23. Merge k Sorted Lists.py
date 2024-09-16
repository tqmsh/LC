# Question:
# Given an array of k linked-lists, each sorted in ascending , merge all the linked-lists into one
# sorted linked-list and return it.

# Input:
# The input is an array of k linked-lists, where each linked-list is represented as a list of integers
# sorted in ascending order. This input defines the lists that need to be merged into one sorted
# linked-list.

# Output:
# The output is a single sorted linked-list that contains all the elements from the input linked-lists
# merged together in ascending order.
from typing import Optional
from typing import List
from heapq import heappush, heappop

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 
        dummy_head = ListNode()
        current = dummy_head
        priorityQueue = []
        for index, list in enumerate(lists):  
            if list: heappush(priorityQueue, (list.val, index, list)) # 按照 val 排序，如果 val 一样，按照 i 排序，永远碰不到 list
        while priorityQueue: 
            _, index, list = heappop(priorityQueue)  
            current.next = list
            list = list.next
            if list: heappush(priorityQueue, (list.val, index, list)) 
            current = current.next
        return dummy_head.next
    
def main():
    solution = Solution() 
    list1 = array_to_linked_list([1,4,5]) 
    list2 = array_to_linked_list([1,3,4])
    list3 = array_to_linked_list([2,6])
    head = solution.mergeKLists([list1, list2, list3]) 
    print_linked_list(head)

if __name__ == "__main__":
    main()
