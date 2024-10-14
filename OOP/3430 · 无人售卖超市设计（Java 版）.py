from typing import List, Dict, Optional
from collections import defaultdict

class ProductType:
    DRINK = "Drink"; SNACK = "Snack" 
class Product:
    def __init__(self, type: str, name: str, cnt: int, price: int) -> None:
        self.type = type; self.name = name; self.cnt = cnt; self.price = price
    def __repr__(self) -> str:
        return f"Product(type={self.type}, name={self.name}, cnt={self.cnt}, price={self.price})" 
class Request:
    def __init__(self, type: str, name: str, cnt: int) -> None:
        self.type = type; self.name = name; self.cnt = cnt 
class Observer:
    def update(self, display: 'Market', product: Product): pass 
class Subject:
    def add_observer(self, key: str, observer: Observer): pass 
    def remove_observer(self, key: str): pass  
    def notify_observer(self, product: Product) -> None: pass 
class Market(Subject):
    def __init__(self, products: List[Product]):
        self.display: defaultdict[str, List[Product]] = defaultdict(list) # type -> products
        self.storage: defaultdict[str, int] = defaultdict(int) # name -> cnt
        self.observers: defaultdict[str, Observer] = defaultdict(Observer)
        for product in products:
            self.add_if_absent(product)
            self.storage[product.name] = product.cnt 
    def add_observer(self, key: str, observer: Observer): self.observers[key] = observer 
    def remove_observer(self, key: str): del self.observers[key] 
    def notify_observer(self, product: Product):
        for observer in self.observers.values(): observer.update(self, product)  
    def purchase(self, product_purchased: Product): # Observer 会调用这个来买他的东西, product 是新进的货
        # 维持 storage
        self.storage[product_purchased.name] += product_purchased.cnt 
        # 维持 display
        if self.non_exist(product_purchased): self.add_if_absent(product_purchased) 
        else: self.add_if_present(product_purchased)  
    def sale(self, requests: List[Request]):
        for request in requests: self.process_request(request) 
    def process_request(self, request: Request):
        product: Optional[Product] = self.request_to_product(request) # 从展柜里拿 product，看看多少钱 
        if product is None:
            print(f"Buy {request.name} Error: Product does not exist!")
            return # 🟥 EDGE CASE: 请求的产品不存在
        if self.storage[request.name] < request.cnt: print(f"Buy {request.name} Error: Out of stock, please reselect!") 
        else: 
            print(f"Buy {request.cnt} {request.name}. Total price: {product.price * request.cnt}")
            # 维持 storage
            self.storage[product.name] -= request.cnt
            # 维持 display
            product.cnt = self.storage[product.name] 
        if self.need_purchase(product): self.notify_observer(product)  
    def request_to_product(self, request: Request) -> Optional[Product]: 
       for product in self.display[request.type]:
            if product.name == request.name:
                return product 
       return None # 🟥 EDGE CASE: 没有找到对应的产品
    def add_if_absent(self, product: Product): # 放展示窗否
        product_list = self.display[product.type]
        if not any(p.name == product.name for p in product_list):
            self.display[product.type].append(product) 
    def add_if_present(self, product_purchased: Product): # 和 stock 更新, 输入 product 为从 observer 购买的物品，在这里给 display 更新
        for product in self.display[product_purchased.type]: 
            if product.name == product_purchased.name:
                product.cnt = self.storage[product.name]
                return 
    def non_exist(self, product: Product) -> bool: # 窗口有没有
        product_list = self.display[product.type]
        return not any(p.name == product.name for p in product_list) 
    def need_purchase(self, product: Product) -> bool: # 需不需要买
        return self.storage[product.name] < 5

class ProductSupplier(Observer): 
    def update(self, market: Market, product: Product):
        # 进十个货
        market.purchase(Product(product.type, product.name, 10, product.price))
        print(f"Supply {product} to Market")
        print(f"{product.name} in Market Storage: {market.storage[product.name]}") 

class CustomerService:
    def __init__(self, market: Market): self.market = market 
    def show_products(self): 
        print("Available products:")
        for type, products in self.market.display.items():
            print(f"Product Type: {type}")
            for product in products:
                print(product) 
    def buy(self, requests: List[Request]) -> None:
        """Process customer purchase requests."""
        self.market.sale(requests)

# Testing
if __name__ == "__main__":
    # Initialization
    products = [Product(ProductType.DRINK, "Coke", 4, 5), Product(ProductType.SNACK, "Chips", 30, 3)]
    market = Market(products)
    supplier = ProductSupplier()
    market.add_observer("Supplier", supplier)

    # Test #1, Functionality of showing products
    customer_service = CustomerService(market) 
    customer_service.show_products()  # Expected to show Coke and Chips

    # Test #2, Functionality of purchasing a product
    requests = [Request(ProductType.DRINK, "Coke", 5)]
    print("\nProcessing purchase request:")
    customer_service.buy(requests)  # Expected to successfully purchase

    # Test #3, Edge case for purchasing out of stock
    requests = [Request(ProductType.SNACK, "Chips", 35)]
    print("\nProcessing purchase request:")
    customer_service.buy(requests)  # Expected to show out of stock message

    # Test #4, Edge case for non-existent product
    requests = [Request(ProductType.SNACK, "NonExistentSnack", 1)]
    print("\nProcessing purchase request:")
    customer_service.buy(requests)  # Expected to show product does not exist message

    # Test #5, Triggering restock of products
    requests = [Request(ProductType.DRINK, "Coke", 16)]
    print("\nProcessing purchase request:")
    customer_service.buy(requests)  # Expected to trigger restock for Coke

    # Final state of the market
    print("\nFinal market storage:")
    for name, cnt in market.storage.items():
        print(f"{name}: {cnt}")
