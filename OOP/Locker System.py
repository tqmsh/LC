from datetime import datetime
from typing import List, Dict, Optional
from random import Random
from collections import defaultdict

# Exceptions
class LockerAlreadyExistsException(Exception): pass  
class NoSlotAvailableException(Exception): pass 
class SlotAlreadyExistsException(Exception): pass 

# Classes
class Sz:
    def __init__(self, w: float, l: float, h: float): self.w = w; self.l = l; self.h = h
    def canFit(self: 'Sz', other: 'Sz') -> bool: return self.w >= other.w and self.l >= other.l and self.h >= other.h

class Package:
    def __init__(self, sz: Sz, ID: str): self.sz = sz; self.ID = ID

class Contact:
    def __init__(self, email: str, address: str): self.email = email; self.address = address

class Slot:
    def __init__(self, slotID: str, sz: Sz): self.slotID = slotID; self.sz = sz; self.package = None; self.allocation_date = None
    def allocate_slot(self, package: Package):
        if self.package: raise SlotAlreadyExistsException("Slot already exists")
        self.package = package; self.allocation_date = datetime.now()
    def deallocate_slot(self): self.package = None; self.allocation_date = None
    def is_available(self) -> bool: return not self.package

class Locker:
    def __init__(self, locker_ID: str): self.locker_ID = locker_ID; self.slots: List[Slot] = []
    def add_slot(self, slot: Slot): self.slots.append(slot)
    def get_available_slots(self) -> List[Slot]: return [slot for slot in self.slots if slot.is_available()]

class OptRepository:
    def __init__(self): self.slot_ID_to_opt: defaultdict[Optional[str], Optional[str]] = defaultdict(lambda: None)
    def add_otp(self, slot_ID: str, otp: str): self.slot_ID_to_opt[slot_ID] = otp
    def get_otp(self, slot_ID: str) -> str: return self.slot_ID_to_opt[slot_ID]

class Receipt:
    def __init__(self, slot: Slot, package: Package, otp: str, user: 'User'): self.slot = slot; self.package = package; self.otp = otp; self.user = user

class LockerSystem:
    def __init__(self): 
        self.lockers: defaultdict[Optional[str], Optional[Locker]] = {} 
        self.otp_generator = RandomOtpGenerator()
        self.otp_repository = OptRepository()
        self.slot_filter_strat = SlotFilterStrategyBySize()
        self.slot_assign_strat = SlotAssignmentStrategyRandom()
    def add_locker(self, locker: Locker):
        if locker.locker_ID in self.lockers: raise LockerAlreadyExistsException()
        self.lockers[locker.locker_ID] = locker
    def allocate_slot(self, package: Package, user: 'User'):
        for locker in self.lockers.values(): 
            avail = self.slot_filter_strat.filter_slots(locker.get_available_slots(), package) 
            if avail: 
                slot = self.slot_assign_strat.pick_slot(avail)
                slot.allocate_slot(package)
                otp = self.otp_generator.generate_otp()
                self.otp_repository.add_otp(slot.slotID, otp)
                return Receipt(slot, package, otp, user)
        return NoSlotAvailableException()
    def get_available_slots(self) -> List[Slot]:
        avail = []
        for locker in self.lockers.values(): avail.extend(locker.get_available_slots())
        return avail
    def validate_otp(self, slot: Slot, otp: str): return self.otp_repository.get_otp(slot.slotID) == otp 
    def deallocate_slot(self, receipt: Receipt):  
        if self.validate_otp(receipt.slot, receipt.otp): receipt.slot.deallocate_slot()  
        else: raise ValueError("Invalid OTP")
    def create_slot(self, locker: Locker, sz: Sz): locker.add_slot(Slot(str(len(locker.slots) + 1), sz))
    def generate_otp(self, slot: Slot) -> str:
        otp = self.otp_generator.generate_otp()
        self.otp_repository.add_otp(slot.slotID, otp)
        return otp
    def notify_user(self, receipt: Receipt):
        user = receipt.user.get_contact()
        print(f"Notif sent to {user} for package {receipt.package.ID}")

# Interfaces
class User:
    def __init__(self, contact: Contact): self.contact = contact
    def get_contact(self) -> Contact: return self.contact

class Buyer(User):
    def __init__(self, contact: Contact): super().__init__(contact) 

class DeliveryPerson(User):
    def __init__(self, contact: Contact): super().__init__(contact)
           
class OtpGenerator:
    def generate_otp(self) -> str: pass

class RandomOtpGenerator(OtpGenerator):
    otp_len: int = 6
    def __init__(self): self.rng = Random()
    def generate_otp(self) -> str: return "".join(self.rng.choices("1234567890", k=self.otp_len))

class SlotFilterStrategy:
    def filter_slots(self, slots: List[Slot], package: Package) -> List[Slot]: pass

class SlotFilterStrategyBySize(SlotFilterStrategy):
    def filter_slots(self, slots: List[Slot], package: Package) -> List[Slot]: return [slot for slot in slots if slot.sz.canFit(package.sz)]

class SlotAssignmentStrategy:
    def pick_slot(self, slots: List[Slot]) -> Slot: pass

class SlotAssignmentStrategyRandom(SlotAssignmentStrategy):
    def __init__(self): self.rng = Random()
    def pick_slot(self, slots: List[Slot]) -> Slot: return self.rng.choice(slots)

def run_tests():
    # Helper function to print test results
    def assert_equal(actual, expected, message):
        assert actual == expected, f"{message}. Expected {expected}, got {actual}"

    # Test Sz class
    size1 = Sz(10, 10, 10)
    size2 = Sz(20, 20, 20)
    assert_equal(size1.canFit(size1), True, "Size can fit itself")
    assert_equal(size1.canFit(size2), False, "Smaller size cannot fit larger size")
    assert_equal(size2.canFit(size1), True, "Larger size can fit smaller size")

    # Test Package class
    package1 = Package(size1, "Package1")
    assert_equal(package1.sz, size1, "Package size")
    assert_equal(package1.ID, "Package1", "Package ID")

    # Test Contact and User classes
    contact1 = Contact(email="buyer@example.com", address="123 Example St")
    buyer = Buyer(contact1)
    assert_equal(buyer.get_contact().email, "buyer@example.com", "Buyer's contact email")
    assert_equal(buyer.get_contact().address, "123 Example St", "Buyer's contact address")
    
    delivery_contact = Contact(email="delivery@example.com", address="456 Delivery St")
    delivery_person = DeliveryPerson(delivery_contact)
    assert_equal(delivery_person.get_contact().email, "delivery@example.com", "Delivery person's contact email")

    # Test Slot class
    slot1 = Slot("1", size1)
    assert_equal(slot1.slotID, "1", "Slot ID")
    assert_equal(slot1.is_available(), True, "Slot is available by default")
    
    slot1.allocate_slot(package1)
    assert_equal(slot1.is_available(), False, "Slot is not available after allocation")
    assert_equal(slot1.package, package1, "Slot package after allocation")

    try:
        slot1.allocate_slot(package1)
    except SlotAlreadyExistsException:
        print("Passed SlotAlreadyExistsException test")

    slot1.deallocate_slot()
    assert_equal(slot1.is_available(), True, "Slot is available after deallocation")
    
    # Test Locker class
    locker = Locker("Locker1")
    assert_equal(locker.locker_ID, "Locker1", "Locker ID")
    
    locker.add_slot(slot1)
    assert_equal(len(locker.get_available_slots()), 1, "Locker has one available slot")
    
    slot2 = Slot("2", size2)
    locker.add_slot(slot2)
    assert_equal(len(locker.get_available_slots()), 2, "Locker has two available slots")

    # Test OTP Generation
    otp_generator = RandomOtpGenerator()
    otp = otp_generator.generate_otp()
    assert_equal(len(otp), 6, "OTP length is correct")
    
    # Test OtpRepository
    otp_repo = OptRepository()
    otp_repo.add_otp(slot1.slotID, otp)
    assert_equal(otp_repo.get_otp(slot1.slotID), otp, "OTP stored correctly")

    # Test LockerSystem end-to-end
    locker_system = LockerSystem()
    locker_system.add_locker(Locker("Locker1"))
    
    locker_system.create_slot(locker_system.lockers["Locker1"], size1)
    locker_system.create_slot(locker_system.lockers["Locker1"], size2)
    
    receipt = locker_system.allocate_slot(package1, buyer)
    assert_equal(receipt.package, package1, "Package in receipt is correct")
    assert_equal(receipt.user.get_contact().email, "buyer@example.com", "Receipt user is correct")

    locker_system.notify_user(receipt)

    # Test Slot
    # Test Slot deallocation with OTP validation
    otp = locker_system.generate_otp(receipt.slot)
    assert locker_system.validate_otp(receipt.slot, otp), "OTP validation successful"
    
    receipt.otp = otp
    locker_system.deallocate_slot(receipt)
    assert_equal(receipt.slot.is_available(), True, "Slot is available after deallocation with OTP")
    try:
        locker_system.allocate_slot(package1, buyer)
        print("Passed re-allocation test")
    except NoSlotAvailableException:
        print("Failed re-allocation test")

    print("All tests passed.")

# Run the tests
run_tests()
