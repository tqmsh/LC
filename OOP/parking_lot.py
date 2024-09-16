from enum import Enum
from typing import Optional, List
from random import choice

class VehicleType(Enum): CAR = 1; BIKE = 2; BUS = 3

class Vehicle:
    def __init__(self, plate: str, company: str, type: VehicleType): self.plate = plate; self.company = company; self.type = type
    def getType(self) -> VehicleType: return self.type
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehicle): return False
        return all([self.plate == other.plate, self.company == other.company, self.type == other.type])

class Car(Vehicle):
    def __init__(self, plate: str, company: str): super().__init__(plate, company, VehicleType.CAR)

class Bike(Vehicle):
    def __init__(self, plate: str, company: str): super().__init__(plate, company, VehicleType.BIKE)

class Bus(Vehicle):
    def __init__(self, plate: str, company: str): super().__init__(plate, company, VehicleType.BUS)

class Slot:
    def __init__(self, lane: int, id: int, type: VehicleType): self.lane = lane; self.id = id; self.type = type; self.vehicle: Optional[Vehicle] = None
    def isAvail(self) -> bool: return self.vehicle is None
    def park(self, vehicle: Vehicle) -> bool: 
        if vehicle.type == self.type and self.isAvail(): 
            self.vehicle = vehicle
            return True
        return False
    def removeVehicle(self) -> Optional[Vehicle]:
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle
    def getVehicle(self) -> Optional[Vehicle]: return self.vehicle

class Lvl:
    def __init__(self, lvl: int, numSlots: int): 
        self.lvl = lvl; self.slotsPerLane: int = 10; self.lanes: int = numSlots // self.slotsPerLane 
        self.slots: List[Slot] = [Slot(lane, i, choice(list(VehicleType))) for lane in range(self.lanes) for i in range(self.slotsPerLane)]
    def park(self, vehicle: Vehicle) -> bool:  
        for slot in self.slots: 
            if slot.park(vehicle): return True
        return False
    def remove(self, vehicle: Vehicle) -> bool:
        for slot in self.slots:
            if slot.vehicle == vehicle:
                slot.removeVehicle()
                return True
        return False
    def companyParked(self, name: str) -> List[Vehicle]:
        return [slot.getVehicle() for slot in self.slots if slot.getVehicle() and slot.getVehicle().company == name]

class ParkingLot:
    def __init__(self, numLvl: int, numSlots: int):
        self.lvls: List[Lvl] = [Lvl(i, numSlots) for i in range(numLvl)]
    def parkVehicle(self, vehicle: Vehicle) -> bool:
        for lvl in self.lvls:
            if lvl.park(vehicle): return True
        return False
    def leaveOperation(self, vehicle: Vehicle) -> bool:
        for lvl in self.lvls:
            if lvl.remove(vehicle): return True
        return False
    def companyParked(self, name: str) -> List[Vehicle]:
        ans: List[Vehicle] = []
        for lvl in self.lvls: ans.extend(lvl.companyParked(name))
        return ans


import unittest

class TestParkingLot(unittest.TestCase):

    def test_park(self):
        parkingLotObj = ParkingLot(6, 30)
        res2 = parkingLotObj.parkVehicle(Car("10", "Amazon"))
        res3 = parkingLotObj.parkVehicle(Bike("20", "Amazon"))
        res4 = parkingLotObj.parkVehicle(Bus("30", "Microsoft"))

        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)

    def test_leave_operation(self):
        parkingLotObj = ParkingLot(6, 30)
        self.assertTrue(parkingLotObj.parkVehicle(Car("20", "Google")))
        self.assertTrue(parkingLotObj.leaveOperation(Car("20", "Google")))
        self.assertFalse(parkingLotObj.leaveOperation(Car("20", "Google")))

    def test_companyParked(self):
        parkingLotObj = ParkingLot(6, 30)
        parkingLotObj.parkVehicle(Car("20", "Google"))
        self.assertEqual(parkingLotObj.companyParked("Google"), [Car("20", "Google")])

    def test_all(self):
        parkingLotObj = ParkingLot(3, 10)
        self.assertTrue(parkingLotObj.parkVehicle(Car("10", "Google")))
        self.assertEqual(parkingLotObj.companyParked("Google"), [Car("10", "Google")])
        self.assertTrue(parkingLotObj.leaveOperation(Car("10", "Google")))
        self.assertEqual(parkingLotObj.companyParked("Google"), [])

if __name__ == '__main__':
    unittest.main()
