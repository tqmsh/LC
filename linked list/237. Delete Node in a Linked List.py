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
    def deleteNode(self, node: ListNode) -> None:
        node.val, node.next = node.next.val, node.next.next

def main():
    # Convert array to linked list
    arr = [4, 5, 1, 9]
    head = array_to_linked_list(arr)
    
    # Print the original linked list
    print("Original linked list:")
    print_linked_list(head)
    
    # Find the node to delete (node with value 5)
    current = head
    while current and current.val != 5:
        current = current.next
    
    if current:
        # Delete the node
        solution = Solution()
        solution.deleteNode(current)
    
    # Print the linked list after deletion
    print("Linked list after deletion:")
    print_linked_list(head)

if __name__ == "__main__":
    main()
