from typing import Optional, Dict
from collections import defaultdict
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp: defaultdict[Optional[Node], Optional[Node]]= defaultdict(lambda: None)
        i = head
        while i:
            mp[i] = Node(i.val)
            i = i.next 
        i = head
        while i:
            mp[i].next = mp[i.next]
            mp[i].random = mp[i.random]
            i = i.next 
        return mp[head]
def build_linked_list(arr):
    if not arr:
        return None
    
    nodes = [Node(val) for val, _ in arr]
    for i, (_, random_index) in enumerate(arr):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    
    return nodes[0]

def print_linked_list(head):
    result = []
    node = head
    while node:
        random_index = None
        if node.random:
            random_index = get_node_index(head, node.random)
        result.append([node.val, random_index])
        node = node.next
    print(result)
 
def get_node_index(head, node):
    index = 0
    while head:
        if head == node:
            return index
        head = head.next
        index += 1
    return None
 
head = build_linked_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
solution = Solution()
copied_head = solution.copyRandomList(head)

# Output the copied list
print_linked_list(copied_head)
