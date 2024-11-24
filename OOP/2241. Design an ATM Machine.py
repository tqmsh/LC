from typing import List
class ATM:
    bank = [0] * 5
    val = [20, 50, 100, 200, 500]
    def deposit(self, inn: List[int]): self.bank = [a + b for a, b in zip(self.bank, inn)]
    def withdraw(self, req: int):
        ans = [0] * 5
        for i in range(4, -1, -1): 
            ans[i] = min(req // self.val[i], self.bank[i]) 
            req -= ans[i] * self.val[i]
            
        if req: return [-1]
        self.bank = [a - b for a, b in zip(self.bank, ans)]
        return ans
