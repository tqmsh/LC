class ListNode:
    def __init__(self, val=0, next=None, pre=None):
        self.val = val
        self.next: ListNode = next
        self.pre: ListNode = pre 

class Solution:
    def generate_min_number(self, sequence): 
        sequence = "i" + sequence   
        ans: ListNode = ListNode(); x: ListNode = ListNode(1); ans.next = x; x.pre = ans    
        lst_dec: ListNode = None   
        
        for i in range(1, len(sequence)): 
            val = i + 1; nxt = ListNode(val)    
            if sequence[i] == 'i':
                x.next = nxt; nxt.pre = x  # x <-> nxt
                x = x.next 
            elif sequence[i] == 'd':
                if sequence[i - 1] == 'i': # x.pre <-> nxt <-> x
                    nxt.next = x; nxt.pre = x.pre
                    x.pre.next = nxt; x.pre = nxt
                    lst_dec = nxt 
                else: # lst.pre <-> nxt <-> lst
                    nxt.next = lst_dec; nxt.pre = lst_dec.pre
                    lst_dec.pre.next = nxt; lst_dec.pre = nxt
                    lst_dec = nxt 
        return ans.next   
    
    def print_list(self, head):
        result = []
        while head:
            result.append(str(head.val))
            head = head.next
        print(" -> ".join(result))

# Example usage:
solution = Solution()
sequence = "iidddd"
head = solution.generate_min_number(sequence)
solution.print_list(head)
