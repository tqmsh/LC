# 在面向对象设计中，中介者模式通过集中管理对象之间的通信，减少对象间的直接依赖，从而促进松耦合。
class AbstractMediator:
    def setPurchase(self, purchase): self.purchase: PurchaseColleague = purchase
    def setWarehouse(self, warehouse): self.warehouse: WarehouseColleague = warehouse
    def setSales(self, sales): self.sales: SalesColleague = sales
    def execute(self, content, num): pass

class StockMediator(AbstractMediator):
    def execute(self, content, num):
        print(f"MEDIATOR: Get Info--{content}")
        if content == 'buy':
            self.warehouse.inc(num)
            self.sales.getNotice(f"Bought {num}")
        elif content == 'increase':
            self.sales.getNotice(f"Inc {num}")
            self.purchase.getNotice(f"Inc {num}")
        elif content == 'decrease':
            self.sales.getNotice(f'Dec {num}')
            self.purchase.getNotice(f'Dec {num}')
        elif content == 'warning':
            self.sales.getNotice(f'Stock is LOW. {num} Left')
            self.purchase.getNotice(f'Stock is LOW. Please buy more! {num} Left')
        elif content == 'sell':
            self.warehouse.dec(num)
            self.purchase.getNotice(f"Sold {num}")
    
class Colleague: 
    def __init__(self, mediator): self.mediator: StockMediator = mediator

class PurchaseColleague(Colleague):
    def buyStuff(self, num):
        print(f"PURCHASE: Bought {num}")
        self.mediator.execute('buy', num)
    def getNotice(self, content): print(f"PURCHASE: Get Notice--{content}")

class WarehouseColleague(Colleague):
    def __init__(self, mediator):
        super().__init__(mediator)
        self.tot = 0; self.threshold = 100
    def setThreshold(self, threshold): self.threshold = threshold
    def isEnough(self):
        if self.tot < self.threshold: 
            print('WAREHOUSE: Warning.. Stock is low')
            self.mediator.execute('warning', self.tot)  # Corrected `self.total` to `self.tot`
        else: return 1
    def inc(self, num): 
        self.tot += num
        print(f"WAREHOUSE: Increase {num}")
        self.mediator.execute('increase', num)
        self.isEnough()
    def dec(self, num):
        self.tot -= num
        print(f"WAREHOUSE: Decrease {num}")
        self.mediator.execute('decrease', num)
        self.isEnough()
    
class SalesColleague(Colleague):
    def sellStuff(self, num):
        print(f"SALES: Sell {num}")
        self.mediator.execute('sell', num)
    def getNotice(self, content): print(f"SALES: Get Notice--{content}")

# Testing the system
if __name__ == "__main__":
    mediator = StockMediator()
    
    purchase = PurchaseColleague(mediator)
    warehouse = WarehouseColleague(mediator)
    sales = SalesColleague(mediator)
    mediator.setPurchase(purchase)
    mediator.setWarehouse(warehouse)
    mediator.setSales(sales)
    
    # Test the workflow
    purchase.buyStuff(300)
    sales.sellStuff(120)
