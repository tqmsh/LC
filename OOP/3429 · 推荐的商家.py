from collections import defaultdict
from typing import List
class Customer:
    def __init__(self, name, pos): self.name = name; self.pos = pos

class Merchant:
    def __init__(self, name: str, pos): self.name = name; self.pos = pos

class Order:
    def __init__(self, customer: Customer, merchant: Merchant, t: int):
        self.customer = customer; self.merchant = merchant; self.t = t

class Platform:
    def __init__(self):
        self.orders: defaultdict[Customer, List[Order]] = defaultdict(list); self.customer: set[Customer] = set(); self.merchants: set[Merchant] = set()
    
    def addCustomer(self, customer): self.customer.add(customer)
    def addMerchant(self, merchant): self.merchants.add(merchant)
    
    def log(self, customer, merchant, t):
        self.addCustomer(customer); self.addMerchant(merchant)
        self.orders[customer].append(Order(customer, merchant, t))
    
    def printCustomerLog(self, customer: Customer):
        for x in sorted(self.orders[customer], key = lambda x : -x.t):
            print(f'ORDER: customer: {x.customer.name}, merchant: {x.merchant.name}, at: {x.t}')

    def recommand(self, customer: Customer):
        ans: List[str] = []
        vis: set[str] = set()  
 
        for x in sorted(self.orders[customer], key=lambda x: -x.t):
            if x not in vis:
                vis.add(x.merchant)
                ans.append(x.merchant.name)
                if len(ans) == 3: return ans

        for x in sorted(self.merchants, key=lambda x: abs(x.pos - customer.pos)):
            if x not in vis:
                vis.add(x)
                ans.append(x.name)
                if len(ans) == 3: return ans
        return ans

    
# Initialize Platform
platform = Platform()

# Create Customers and Merchants
customer1 = Customer("Alice", 10)
customer2 = Customer("Bob", 20)
customer3 = Customer("Charlie", 5)

merchant1 = Merchant("BookStore", 15)
merchant2 = Merchant("Grocery", 25)
merchant3 = Merchant("Cafe", 8)
merchant4 = Merchant("Electronics", 30)

# Log Orders
platform.log(customer1, merchant1, 5)   # Alice orders from BookStore at time 5
platform.log(customer1, merchant2, 10)  # Alice orders from Grocery at time 10
platform.log(customer1, merchant3, 15)  # Alice orders from Cafe at time 15

platform.log(customer2, merchant2, 12)  # Bob orders from Grocery at time 12
platform.log(customer2, merchant4, 18)  # Bob orders from Electronics at time 18

platform.log(customer3, merchant3, 20)  # Charlie orders from Cafe at time 20

# Test Recommendations
print("Recommendations for Customer 1 (Alice):")
print(platform.recommand(customer1))  # Expected: ['Cafe', 'Grocery', 'BookStore']

print("\nRecommendations for Customer 2 (Bob):")
print(platform.recommand(customer2))  # Expected: ['Electronics', 'Grocery', 'BookStore'] or another nearby merchant if they exist

print("\nRecommendations for Customer 3 (Charlie):")
print(platform.recommand(customer3))  # Expected: ['Cafe', 'BookStore', 'Grocery']
