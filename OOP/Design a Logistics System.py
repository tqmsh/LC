from enum import Enum
from datetime import datetime
from typing import List, Optional
from collections import defaultdict

class VehicleStatus(Enum): FREE = "FREE"; BUSY = "BUSY"; NOT_WORKING = "NOT_WORKING"
class OrderStatus(Enum): DELIVERED = "DELIVERED"; CANCELLED = "CANCELLED"; PROCESSING = "PROCESSING"
class PaymentStatus(Enum): PAID = "PAID"; UNPAID = "UNPAID"
class OrderPriority(Enum): LOW = "LOW"; MEDIUM = "MEDIUM"; HIGH = "HIGH"

class Location:
    def __init__(self, long: float, lat: float): self.long = long; self.lat = lat 
    def __str__(self): return f"Location(longitude={self.long}, latitude={self.lat})"

class Vehicle:
    def __init__(self, id: int, plate: str, v: int, x: Location, status: VehicleStatus):
        self.id = id; self.plate = plate; self.v = v; self.x = x; self.status = status
    def update_location(self, new_location: Location): self.x = new_location
    def update_status(self, new_status: VehicleStatus): self.status = new_status
    def __str__(self): return f"Vehicle(id={self.id}, plate={self.plate}, volume={self.v}, status={self.status})"

class Truck(Vehicle): pass
class Bike(Vehicle): pass

class Item:
    def __init__(self, name: str, price: int, v: int, w: int): self.name = name; self.price = price; self.v = v; self.w = w 
    def __str__(self): return f"Item(name={self.name}, price={self.price}, volume={self.v}, weight={self.w})"

class Client:
    def __init__(self, id: int, name: str, address: Location): self.id = id; self.name = name; self.address = address 
    def __str__(self): return f"Client(id={self.id}, name={self.name}, address={self.address})"

class Order:
    def __init__(self, id: int, items: List[Item], s_name: Client, s_x: Location, e_x: Location, 
                 priority: OrderPriority, orderStatus: OrderStatus, paymentStatus: PaymentStatus, 
                 st: datetime, et: datetime):
        self.id = id; self.items = items; self.s_name = s_name; self.s_x = s_x; self.e_x = e_x
        self.priority = priority; self.orderStatus = orderStatus; self.paymentStatus = paymentStatus
        self.st = st; self.et = et
        self.w = sum(item.w for item in items)
        self.v = sum(item.v for item in items)

class VehicleNotFoundException(Exception): pass
class OrderNotPaidException(Exception): pass  

class Admin:
    def __init__(self):
        self.order_locations = defaultdict(lambda: Location(0.0, 0.0))
        self.vehicles: List[Vehicle] = []

    def pay_order(self, order: Order):
        if order.paymentStatus == PaymentStatus.UNPAID: order.paymentStatus = PaymentStatus.PAID
        else: print(f"Order {order.id} already paid for") 

    def take_order(self, order: Order):
        if order.paymentStatus == PaymentStatus.UNPAID: 
            raise OrderNotPaidException
        self.order_locations[order.id] = order.s_x
        print(f"Order {order.id} taken with destination at {order.s_x}") 

    def complete_order(self, order: Order):
        if order.id not in self.order_locations:
            print(f"Order {order.id} cannot be completed because it was not taken.")
            return
        if order.orderStatus == OrderStatus.CANCELLED:
            print(f"Order {order.id} cannot be completed because it is cancelled.")
            return
        if order.orderStatus != OrderStatus.DELIVERED:
            try:
                vehicle = self.assign_vehicle(order)
                vehicle.update_location(order.e_x)
                print(f"Order {order.id} assigned to vehicle {vehicle.plate}.")
                order.orderStatus = OrderStatus.DELIVERED
                self.order_locations[order.id] = order.e_x
                print(f"Order {order.id} has been delivered.")
            except VehicleNotFoundException as e:
                print(e)
        else:
            print(f"Order {order.id} is already delivered.")

    def track_order(self, order_id: int) -> Location:
        location = self.order_locations[order_id]
        print(f"Order {order_id} is at {location}")
        return location

    def assign_vehicle(self, order: Order) -> Optional[Vehicle]:
        for vehicle in self.vehicles:
            if vehicle.status == VehicleStatus.FREE and vehicle.v >= order.v:
                vehicle.update_status(VehicleStatus.BUSY)
                print(f"Assigned {vehicle} to order {order.id}")
                return vehicle
        raise VehicleNotFoundException(f"No available vehicle for order {order.id}")

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        print(f"Added vehicle {vehicle}")

# Test cases
if __name__ == "__main__":
    loc1 = Location(1.0, 2.0)
    loc2 = Location(3.0, 4.0)
    loc3 = Location(5.0, 6.0)
    loc4 = Location(7.0, 8.0)

    bike1 = Bike(1, "BIKE1", 10, loc1, VehicleStatus.FREE)
    truck1 = Truck(2, "TRUCK1", 50, loc2, VehicleStatus.FREE)

    item1 = Item("Item1", 100, 5, 10)
    item2 = Item("Item2", 200, 10, 20)

    client1 = Client(1, "Client1", loc3)
    client2 = Client(2, "Client2", loc4)

    order2 = Order(2, [item1], client2, loc2, loc3, OrderPriority.LOW, OrderStatus.PROCESSING, PaymentStatus.UNPAID, datetime.now(), datetime.now())

    admin = Admin()
    admin.add_vehicle(bike1)
    admin.add_vehicle(truck1)

    admin.take_order(order2)
    admin.complete_order(order2)
