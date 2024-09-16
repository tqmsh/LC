from datetime import datetime
from enum import Enum
from typing import List, Dict, Union, Optional
from collections import defaultdict 

# <<ENUMS>>
class FlightStatus(Enum):
    ACTIVE = 'Active'; SCHEDULED = 'Scheduled'; DELAYED = 'Delayed'; DEPARTED = 'Departed'; LANDED = 'Landed'; IN_AIR = 'InAir'; ARRIVED = 'Arrived'; CANCELED = 'Canceled'; UNKNOWN = 'Unknown'
class SeatClass(Enum):
    ECONOMY = 'Economy'; ECONOMY_PLUS = 'EconomyPlus'; PREFERRED_ECONOMY = "PreferredEconomy"; BUSINESS = "Business"; FIRST_CLASS = "FirstClass"
class SeatType(Enum):
    REGULAR = 'Regular'; ACCESSIBLE = "Accessible"; EMERGENCY_EXIT = "EmergencyExit"; EXTRA_LEG_ROOM = "ExtraLegRoom"
class ReservationStatus(Enum):
    REQUESTED = 'Requested'; PENDING = 'Pending'; CONFIRMED = 'Confirmed'; CHECKED_IN = 'CheckedIn'; CANCELED = 'Canceled'

# <<Classes>
class Airport:
    def __init__(self, name: str, address: str, code: str): self.name = name; self.address = address;  self.code = code
class Seat:
    def __init__(self, id: str, type: SeatType, class_: SeatClass): self.id = id; self.type = type; self.class_ = class_
class Aircraft:
    def __init__(self, name: str, model: str, seats: List[Seat]): self.name = name; self.model = model; self.seats = seats
class Passenger:
    def __init__(self, name: str, email: str): self.name = name; self.email = email
class Flight:
    def __init__(self, id: str, s: Airport, e: Airport, dt: int, aircraft: Aircraft): self.id = id; self.s = s; self.e = e; self.dt = dt; self.aircraft = aircraft
    def get_avail_seats(self, r: 'ReservationRequest') -> List[Seat]: pass
    def get_price(self, seat: Seat) -> float: pass
class FlightInstance (Flight):
    def __init__(self, id: str, s: Airport, e: Airport, dt: int, aircraft: Aircraft, t: datetime, gate: str, status: FlightStatus, seats: List[Seat], crew: List[str] = []):
        super().__init__(id, s, e, dt, aircraft)
        self.t = t; self.gate = gate; self.status = status; self.seats = seats; self.crew = crew; self.cost: defaultdict[Seat, float] = defaultdict(float); self.reservations: List['Reservation'] = []
    def get_avail_seats(self, r: 'ReservationRequest') -> List[Seat]: # ReservationRequest 里的座位哪一些可以满足
        avail = [seat for seat in self.seats if seat not in [res.seat for res in self.reservations]]
        ans = []
        for class_, mp in r.seat_needed.items():
            for type, cnt in mp.items():
                tmp = [seat for seat in avail if seat.class_ == class_ and seat.type == type]
                ans.extend(tmp[:cnt])  
        return ans
    def get_price(self, seat: Seat) -> float: return self.cost[seat]
class Reservation:
    def __init__(self, id: str, flight: FlightInstance, passenger: Passenger, seat: Seat, status: ReservationStatus): self.id = id; self.flight = flight; self.passenger = passenger; self.seat = seat; self.status = status
    def checkIn(self, passenger: Passenger): 
        if self.passenger == passenger: self.status = ReservationStatus.CHECKED_IN; return 1
        return 0
class ReservationRequest: 
    def __init__(self, flight: FlightInstance, passenger: Passenger, seat_needed: defaultdict[SeatClass, defaultdict[SeatType, int]]): self.flight = flight; self.passenger = passenger; self.seat_needed = seat_needed 
class Airline:
    def __init__(self, name: str, code: str, flights: List[Flight], aircrafts: List[Aircraft]): self.name = name; self.code = code; self.flights = flights; self.aircrafts = aircrafts
class Payment:
    def __init__(self, amt: float): self.amt = amt
class Ininerary: # 把一画好的行程付款
    def __init__(self, s: Airport, e: Airport, t: datetime, reservations: List[Reservation], payment: Payment): self.s = s; self.e = e; self.t = t; self.reservations = reservations; self.payment = payment
    def make_reservations(self, reservations: List[Reservation]):  self.reservations.extend(reservations)
    def make_payment(self, payment: Payment): 
        total_cost = sum(reservation.flight.get_price(reservation.seat) for reservation in self.reservations)
        if payment.amt >= total_cost:
            self.payment = payment
            for reservation in self.reservations:
                reservation.status = ReservationStatus.CONFIRMED
        else:
            raise ValueError("Payment not sufficient to cover all reservations")
class AirlineManagementSystem:
    def __init__(self):
        self.airports: List[Airport] = []; self.airlines: List[Airline] = []; self.flights: List[FlightInstance] = [];  self.reservations: List[Reservation] = []
    def add_airline(self, airline: Airline): self.airlines.append(airline)
    def remove_airline(self, airline: Airline): self.airlines.remove(airline)
    def add_flight(self, flight: Flight): self.flights.append(flight)
    def modify_flight(self, flight: Flight):
        for i, f in enumerate(self.flights):
            if f.id == flight.id: self.flights[i] = flight; return
    def cancel_flight(self, flight: Flight): self.flights.remove(flight)
    def search_flights(self, spec: Dict[str, Union[str, datetime]], param: Dict[str, Union[str, datetime]]) -> List[Flight]:
        ans = []
        for flight in self.flights:
            f = 1
            for k in spec:
                if getattr(flight, k) != param[k]: f = 0; break
            if f: ans.append(flight)
        return ans
    def get_avail_seats(self, req: ReservationRequest) -> List[Seat]: return req.flight.get_avail_seats(req)
    def make_reservation(self, req: ReservationRequest) -> Reservation:
        avail = self.get_avail_seats(req) # 先把该航班里的位置拿出来
        if len(avail) < sum(sum(mp.values()) for mp in req.seat_needed.values()): raise ValueError("Not enough seats available") # 够么？
        seat = avail[0]
        reservation = Reservation(f'{req.flight.id}-{req.passenger.name}', req.flight, req.passenger, seat, ReservationStatus.PENDING)
        self.reservations.append(reservation) # 录总部
        req.flight.reservations.append(reservation) # 录飞机
        return reservation # 合法，给 Pending
    def modify_reservation(self, r: Reservation):
        for i, res in enumerate(self.reservations):
            if res.id == r.id: self.reservations[i] = r; return 
    def cancel_reservation(self, r: Reservation):
        self.reservations.remove(r) 
        r.status = ReservationStatus.CANCELED
    def create_itinerary(self, payment: Payment, reservations: List[Reservation]) -> Ininerary:
        if not reservations: raise ValueError('bad reservation, nothing to include')
        reservations.sort(key = lambda r: (r.flight.s, r.flight.e))
        s = reservations[0].flight.s
        e = reservations[-1].flight.e
        t = reservations[0].flight.t
        itinerary = Ininerary(s, e, t, reservations, payment)
        itinerary.make_payment(payment)   
        return itinerary 
    def make_payment(self, amt: float) -> Payment: return Payment(amt)
    def assign_crew(self, crew: List[str], flight: FlightInstance): flight.crew.extend(crew)
    def check_in(self, reservation: Reservation, passenger: Passenger) -> bool: return reservation.checkIn(passenger)

import unittest
from datetime import datetime

class TestAirlineManagementSystem(unittest.TestCase):

    def setUp(self):
        self.ams = AirlineManagementSystem()

        # Create airports
        self.airport1 = Airport("Airport A", "Address A", "AAA")
        self.airport2 = Airport("Airport B", "Address B", "BBB")
        self.ams.airports.extend([self.airport1, self.airport2])

        # Create seats
        self.seats = [Seat(f"{i+1}", SeatType.REGULAR, SeatClass.ECONOMY) for i in range(5)]
        
        # Create an aircraft
        self.aircraft = Aircraft("Boeing 737", "737", self.seats)
        
        # Create a flight instance with seats
        self.flight_instance1 = FlightInstance(
            "FL123", self.airport1, self.airport2, 60, self.aircraft,
            datetime(2023, 5, 10, 15, 30), "G01", FlightStatus.SCHEDULED, self.seats
        )

        self.flight_instance2 = FlightInstance(
            "FL456", self.airport2, self.airport1, 60, self.aircraft,
            datetime(2023, 5, 11, 16, 30), "G02", FlightStatus.DELAYED, self.seats
        )

        self.ams.add_flight(self.flight_instance1)
        self.ams.add_flight(self.flight_instance2)
        
        # Create a passenger
        self.passenger = Passenger("John Doe", "john.doe@example.com")

    def test_search_flights(self):
        # Search for a flight by departure airport and status
        search_spec = {"s": self.airport1, "status": FlightStatus.SCHEDULED}
        search_param = {"s": self.airport1, "status": FlightStatus.SCHEDULED}
        result = self.ams.search_flights(search_spec, search_param)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, "FL123")

        # Search for a flight by arrival airport and status
        search_spec = {"e": self.airport1, "status": FlightStatus.DELAYED}
        search_param = {"e": self.airport1, "status": FlightStatus.DELAYED}
        result = self.ams.search_flights(search_spec, search_param)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, "FL456")

        # Search for a flight with a combination of criteria
        search_spec = {"s": self.airport2, "status": FlightStatus.DELAYED, "gate": "G02"}
        search_param = {"s": self.airport2, "status": FlightStatus.DELAYED, "gate": "G02"}
        result = self.ams.search_flights(search_spec, search_param)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, "FL456")

        # Search for a non-existing flight
        search_spec = {"s": self.airport1, "status": FlightStatus.DELAYED}
        search_param = {"s": self.airport1, "status": FlightStatus.DELAYED}
        result = self.ams.search_flights(search_spec, search_param)
        
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()
