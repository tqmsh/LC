# 实物类
# Inputs and Outputs, Applicable Design Patterns, state Pattern, Decorator Pattern, Factory Pattern
from collections import defaultdict
from typing import List, Tuple
from enum import Enum
class NotEnoughItemException(Exception): pass
class notEnoughMoneyException(Exception): pass
class Coin(Enum): PENNY = 1; NICKLE = 5; DIME = 10; QUARTER = 25; DOLLAR = 100; LOONIE = 200
class ItemInfo:
    def __init__(self, price: float = -1, name: str = None): 
        self.price = price
        self.name = name  
class Item:
    def __init__(self, info: ItemInfo): self.info = info
class Stock:
    def __init__(self): self.stock: defaultdict[ItemInfo, List[Item]] = defaultdict(list)
    def get_qty(self, info: ItemInfo): return len(self.stock[info])
    def add_item(self, item: Item): self.stock[item.info].append(item)
    def reduce_item_type(self, itemInfo: ItemInfo): 
        if not self.get_qty(itemInfo): raise NotEnoughItemException(f'lack of {itemInfo.name} in stock')  
        self.stock[itemInfo].pop()
class State:
    def select_item(self, selection: str) -> float: pass
    def take_coins(self, coins: List[Coin]): pass
    def execute_transaction(self) -> Tuple[Item, List[Coin]]: pass
    def cancel_transaction(self) -> List[Coin]: pass

class NoSelectionState(State): 
    def __init__(self, vendingMachine: 'VendingMachine'): self.vendingMachine = vendingMachine
    def select_item(self, selection: str) -> float:
        if selection in self.vendingMachine.name_to_itemInfo:
            self.vendingMachine.now_itemInfo = self.vendingMachine.name_to_itemInfo[selection] # (1) 维持 now_
            self.vendingMachine.state = self.vendingMachine.hasSelectionState # (2) 维持 state
            return self.vendingMachine.now_itemInfo.price # (3) 返回钱
        else: raise ValueError('bad selection')
    def take_coins(self, coins: List[Coin]): raise Exception('No item selected')
    def execute_transaction(self) -> Tuple[Item | List[Coin]]: raise Exception('No item selected')
    def cancel_transaction(self) -> List[Coin]: raise Exception('No item selected')

class HasSelectionState(State):
    def __init__(self, vendingMachine: 'VendingMachine'): self.vendingMachine = vendingMachine
    def select_item(self, selection: str) -> float: raise Exception('Item alr selected')
    def take_coins(self, coins: List[Coin]): self.vendingMachine.now_coins.extend(coins)
    def execute_transaction(self)  -> Tuple[Item | List[Coin]]:
        tot = sum(coin.value for coin in self.vendingMachine.now_coins)
        if tot < self.vendingMachine.now_itemInfo.price: raise notEnoughMoneyException('Lack of Money') 
        req = tot - self.vendingMachine.now_itemInfo.price # (1) 找钱
        ans: list[Coin] = []
        coins = sorted(Coin, key = lambda x: -x.value)      
        for coin in coins:
            while req >= coin.value:
                ans.append(coin)
                req -= coin.value
        self.vendingMachine.coins.extend(self.vendingMachine.now_coins)
        self.vendingMachine.stock.reduce_item_type(self.vendingMachine.now_itemInfo) # (2) 维持类变量
        self.vendingMachine.state = self.vendingMachine.noSelectionState 
        tmp = self.vendingMachine.now_itemInfo.name
        self.vendingMachine.now_itemInfo = None
        self.vendingMachine.now_coins = []
        return (tmp, ans)
class VendingMachine:
    def __init__(self):
        self.coins: List[Coin] = []; self.stock: Stock = Stock()
        self.name_to_itemInfo: defaultdict[str, ItemInfo] = defaultdict(ItemInfo)

        self.noSelectionState: NoSelectionState = NoSelectionState(self)
        self.hasSelectionState: HasSelectionState = HasSelectionState(self)
        self.state: State = self.noSelectionState  

        self.now_itemInfo: ItemInfo = None; self.now_coins: List[Coin] = []
    def select_item(self, selection: str) -> float: return self.state.select_item(selection)
    def take_coins(self, coins: List[Coin]): return self.state.take_coins(coins)
    def execute_transaction(self) -> Tuple[Item, List[Coin]]: return self.state.execute_transaction()
    def cancel_transaction(self): return self.state.cancel_transaction()
    def refill_items(self, items: List[Item]):
        for item in items: 
            self.stock.add_item(item)
            self.name_to_itemInfo[item.info.name] = item.info
    def refund(self):
        tmp = self.now_coins.copy()
        self.now_coins = []
        self.state = self.noSelectionState
        return tmp
    
# Initialize Vending Machine
vending_machine = VendingMachine()

# Refill the vending machine with items
items_to_add = [
    Item(ItemInfo(150, 'Coke')),
    Item(ItemInfo(100, 'Pepsi')),
    Item(ItemInfo(200, 'Water'))
]
vending_machine.refill_items(items_to_add)

# Testing coin insertion and item purchase with correct and incorrect funds
try:
    # Select an item and provide sufficient funds
    print(f'Price of Water: {vending_machine.select_item("Water")}')
    vending_machine.take_coins([Coin.QUARTER])
    item, change = vending_machine.execute_transaction()
    change_display = ', '.join(coin.name for coin in change) if change else 'no change needed'
    print(f'Bought {item} with change: {change_display}')
except Exception as e:
    print(f'Error: {e}')

# Cancel transaction and check refund
refunded_coins = vending_machine.refund()
refunded_display = ', '.join(coin.name for coin in refunded_coins)
print(f'Refunded coins: {refunded_display}')

# Check stock levels for each item after transactions
for item_info in vending_machine.stock.stock:
    stock_count = vending_machine.stock.get_qty(item_info)
    print(f'{item_info.name} stock count: {stock_count}')
