from typing import List
class NoTableForReservationException(Exception): pass

class Meal: 
    def __init__(self, price: float): self._price = price
    def getPrice(self) -> float: return self._price
        
class TimePeriod:
    def __init__(self, start: int, end: int): self._start = start; self._end = end
    def getStart(self) -> int: return self._start
    def getEnd(self) -> int: return self._end

class Table:
    def __init__(self, capacity: int): self.avail = 1; self.capacity = capacity; self.reservations: List[TimePeriod] = []
    def isAvail(self): return self.avail
    def markUnavail(self): self.avail = 0
    def markAvail(self): self.avail = 1
    def getCapacity(self): return self.capacity
    def isAvailableForTimePeriod(self, period: TimePeriod) -> bool:
        for reservation in self.reservations:
            if period.getStart() < reservation.getEnd() and period.getEnd() > reservation.getStart(): return False
        return True

class Party:
    def __init__(self, sz: int):  self._sz = sz
    def getSz(self) -> int: return self._sz 

class Order:
    def __init__(self, meals: List[Meal], table: Table, party: Party): self.meals = meals; self.table = table; self.party = party
    def getPrice(self) -> float: return sum(meal.getPrice() for meal in self.meals)
        
class Reservation:
    def __init__(self, timePeriod: TimePeriod, table: Table): self.timePeriod = timePeriod; self.table = table
        
class Restaurant:
    def __init__(self, tables: List[Table], menu: List[Meal]): self.tables = tables; self.menu = menu; self.orders: List[Order] = []
    def findTable(self) -> Table: 
        for table in self.tables: 
            if table.isAvail(): return table 
        raise NoTableForReservationException
    def takeOrder(self, order: Order): self.orders.append(order)
    def checkout(self, order: Order): self.orders.remove(order); order.table.markAvail()
    def reserveTable(self, timePeriod: TimePeriod, party: Party) -> Reservation:
        for table in self.tables:
            if table.getCapacity() >= party.getSz() and table.isAvailableForTimePeriod(timePeriod):
                table.reservations.append(timePeriod)
                return Reservation(timePeriod, table)
        raise NoTableForReservationException

# Unit Tests
import unittest

class TestRestaurantSystem(unittest.TestCase):
    
    def setUp(self):
        self.tables = [Table(2), Table(4), Table(6)]
        self.menu = [Meal(10.0), Meal(15.0), Meal(20.0)]
        self.restaurant = Restaurant(self.tables, self.menu)
    
    def test_table_availability(self):
        table = self.restaurant.findTable()
        self.assertTrue(table.isAvail())
        table.markUnavail()
        self.assertFalse(table.isAvail())
        table.markAvail()
        self.assertTrue(table.isAvail())
    
    def test_order_price_calculation(self):
        party = Party(2)
        table = self.restaurant.findTable()
        meals = [self.menu[0], self.menu[1]]
        order = Order(meals, table, party)
        self.assertEqual(order.getPrice(), 25.0)
    
    def test_take_order(self):
        party = Party(2)
        table = self.restaurant.findTable()
        meals = [self.menu[0], self.menu[1]]
        order = Order(meals, table, party)
        self.restaurant.takeOrder(order)
        self.assertIn(order, self.restaurant.orders)
    
    def test_checkout(self):
        party = Party(2)
        table = self.restaurant.findTable()
        meals = [self.menu[0], self.menu[1]]
        order = Order(meals, table, party)
        self.restaurant.takeOrder(order)
        self.restaurant.checkout(order)
        self.assertNotIn(order, self.restaurant.orders)
        self.assertTrue(table.isAvail())
    
    def test_no_table_available(self):
        for _ in range(3):  # Reserve all tables
            table = self.restaurant.findTable()
            table.markUnavail()
        with self.assertRaises(NoTableForReservationException):
            self.restaurant.findTable()

    def test_reserve_table(self):
        timePeriod1 = TimePeriod(18, 20)
        timePeriod2 = TimePeriod(19, 21) 
        party = Party(4) 
        self.restaurant.reserveTable(timePeriod1, party) 
        self.restaurant.reserveTable(timePeriod1, party)  
        with self.assertRaises(NoTableForReservationException):
            self.restaurant.reserveTable(timePeriod2, party)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
