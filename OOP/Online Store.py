from typing import List

class Product:
    def __init__(self, name, price, description, stock): 
        self.name = name; self.price = price; self.description = description; self.stock = stock  
    def upd_stock(self, quantity): self.stock += quantity
    def tot_cost(self): return self.stock * self.price
    def __repr__(self): return f"{self.name} (Price: ${self.price}), Stock: {self.stock}"

class Customer:
    def __init__(self, name, email):
        self.name = name; self.email = email; self.orders = []
    def place_order(self, store, product: Product, quantity):
        if product.stock >= quantity: 
            order = Order(self, product, quantity)
            product.upd_stock(-quantity); self.orders.append(order); store.add_order(order)
        else: print(f'not enough stock for {product.name}')
    def view_orders(self): 
        for order in self.orders: print(order)
    def __repr__(self): return f"Customer: {self.name} (Email: {self.email})"

class Order:
    def __init__(self, customer: Customer, product: Product, quantity): 
        self.customer = customer; self.product = product; self.quantity = quantity
    def tot_cost(self): return self.quantity * self.product.price
    def __repr__(self): return f"Order by {self.customer.name}: {self.quantity} x {self.product.name} = $ {self.tot_cost()}"

class Store:
    def __init__(self): 
        self.products: List[Product] = []; self.orders: List[Order] = []; self.customers: List[Customer] = []
    def add_product(self, product: Product): self.products.append(product)
    def del_product(self, product: Product): self.products.remove(product)
    def add_customer(self, customer: Customer): self.customers.append(customer)
    def del_customer(self, customer: Customer): self.customers.remove(customer)
    def add_order(self, order: Order): self.orders.append(order)
    def del_order(self, order: Order): self.orders.remove(order)
    def find_product(self, name):
        for product in self.products: 
            if product.name == name: return product
    def find_customer(self, name):
        for customer in self.customers: 
            if customer.name == name: return customer
    def sales_report(self): return sum(order.tot_cost() for order in self.orders)
    def restock_report(self): return [product for product in self.products if product.stock < 10]
    def __repr__(self): return f"Store w {len(self.products)} products, {len(self.customers)} customers, and {len(self.orders)} orders."

# Test the classes
if __name__ == "__main__":
    store = Store()

    product1 = Product("Keyboard", 49.99, "Wireless keyboard", 10)
    product2 = Product("Mouse", 29.99, "Wireless mouse", 10)
    store.add_product(product1); store.add_product(product2)

    customer1 = Customer("John Smith", "john@example.com")
    customer2 = Customer("Jane Doe", "jane@example.com")
    store.add_customer(customer1); store.add_customer(customer2)

    customer1.place_order(store, product1, 1)
    customer2.place_order(store, product2, 2)

    print("Total sales:", store.sales_report()) #Total sales: 109.97
    print("Low stock:", store.restock_report()) # Low stock: [Keyboard (Price: $49.99), Stock: 9, Mouse (Price: $29.99), Stock: 8]

    customer1.view_orders(); customer2.view_orders()
    # Order by John Smith: 1 x Keyboard = $ 49.99
    # Order by Jane Doe: 2 x Mouse = $ 59.98
    print(store) #Store w 2 products, 2 customers, and 2 orders.
