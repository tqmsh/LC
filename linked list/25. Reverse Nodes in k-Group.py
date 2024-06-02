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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        global s, f, ans, cnt, cont, tail, len
        s = head
        ans = None
        tail = None
        cnt = 0 
        cont = 1
        len = 0
        def one():  
            global s, ans, cnt, cont, tail,len
            # print(s.val, f.val)  
            # 换 s
            tail = s
            tmp1 = s
            L, R = None, None
            for i in range(k): 
                len += 1
                if s and s.next: R = s.next 
                else: cont = 0
                if s: s.next = L # 🟥赋值不用查s.nxt,只用s
                else: cont = 0
                if s: L = s
                if R: s = R 
            if cnt == 0: 
                if L: ans = L 
                cnt += 1
            # 拿地址（如果存在的话）

            if s: tmp2 = s
            for i in range(k - 1): 
                if tmp2 and tmp2.next: 
                    tmp2 = tmp2.next  
                else: 
                    cont = 0
                    return
                    
            # print(tmp2.val)

            if tmp1 and cont: tmp1.next = tmp2  #🟥判断继续
            else:  
                cont = 0
                return
         
        while cont:
            one()

        cur, x = s, 0
        while cur:
            x += 1
            cur = cur.next
        if (len + x) % k != 0: tail.next = s  
        
        return ans

def main():


    solution = Solution()
    head = [1,2,3,4,5]
                #store 4, store 9
    k = 3
    head = array_to_linked_list(head) 
    print_linked_list(solution.reverseKGroup(head, k))

if __name__ == "__main__":
    main()




# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def array_to_linked_list(arr):
#     if not arr:
#         return None
#     head = ListNode(arr[0])
#     xrent = head
#     for value in arr[1:]:
#         xrent.next = ListNode(value)
#         xrent = xrent.next
#     return head

# def print_linked_list(head):
#     xrent = head
#     while xrent:
#         print(xrent.val, end=" -> " if xrent.next else "\n")
#         xrent = xrent.next

# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         s = ListNode(next=head)
#         L = s
#         nodes = self.getKnodes(head, k)
#         while len(nodes) == k:
#             L.next = nodes[-1] 
#             nodes[0].next = nodes[-1].next  

#             # 下一个 k 窗口
#             L = nodes[0]
#             for i in range(1, k):
#                 nodes[i].next = nodes[i-1]

#             nodes = self.getKnodes(nodes[0].next, k)
#         return s.next
    
#     def getKnodes(self, node, k):
#         nodes = []
#         while len(nodes) < k and node is not None:
#             nodes.append(node)
#             node = node.next
#         return nodes

# def main():


#     solution = Solution()
#     head = [1,2,3,4,5]
#                 #store 4, store 9
#     k = 3
#     head = array_to_linked_list(head) 
#     print_linked_list(solution.reverseKGroup(head, k))

# if __name__ == "__main__":
#     main()
