# 多个酒店（如 booking.com）或单个酒店？
# 不同的房间类型具有不同的房间容量和价格
# 列表结果为房间类型，而不是具体的房间号 (如：双人房，而不是501, 502等房间号)

from collections import defaultdict
from typing import List, Tuple
from datetime import date, timedelta
class NotEnoughRoomForReservationException(Exception): pass
    
class RoomType:
    SINGLE = "Single"
    DOUBLE = "Double"

class Room:
    def __init__(self, type: RoomType):
        self.type = type

class ReservationRequest:
    def __init__(self, s: date, e: date, amt: defaultdict[RoomType, int]):
        self.s = s
        self.e = e
        self.amt = amt

class Reservation:
    def __init__(self, s: date, e: date, rooms: List[Room]):
        self.s = s
        self.e = e
        self.rooms = rooms

class Hotel:
    def __init__(self):
        self.rooms: List[Room] = []
        self.reservations: List[Reservation] = []
        self.history: defaultdict[Room, List[date]] = defaultdict(list)

    @staticmethod
    def date_range(s: date, e: date) -> List[date]:
        return [s + timedelta(days=i) for i in range((e - s).days + 1)]

    def log_room(self, room: Room):
        self.rooms.append(room)

    def search(self, req: ReservationRequest, ret_rooms: bool = False) -> Tuple[defaultdict[RoomType, int], List[Room]]:
        avail = defaultdict(int)
        rooms: List[Room] = []

        for room in self.rooms:
            if room.type in req.amt:
                if all(d not in self.history[room] for d in self.date_range(req.s, req.e)):
                    avail[room.type] += 1
                    rooms.append(room)

        if ret_rooms:
            return avail, rooms
        return avail

    def reserve(self, req: ReservationRequest) -> Reservation:
        avail, rooms = self.search(req, ret_rooms=True)

        for type, count in req.amt.items():
            if avail[type] < count:
                raise NotEnoughRoomForReservationException(f"Not enough {type} rooms available.")

        took = []
        for room in rooms:
            if req.amt[room.type] > 0:
                took.append(room)
                self.history[room].extend(self.date_range(req.s, req.e))
                req.amt[room.type] -= 1 

        reserv = Reservation(req.s, req.e, took)
        self.reservations.append(reserv)
        return reserv

    def cancel(self, res: Reservation):
        for room in res.rooms:
            self.history[room] = [d for d in self.history[room] if d < res.s or d > res.e]
        self.reservations.remove(res)

import unittest
from collections import defaultdict
from datetime import date

class TestHotelReservationSystem(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel()
        self.room1 = Room(RoomType.SINGLE)
        self.room2 = Room(RoomType.DOUBLE)
        self.room3 = Room(RoomType.SINGLE)
        self.hotel.log_room(self.room1)
        self.hotel.log_room(self.room2)
        self.hotel.log_room(self.room3)

    def test_log_room(self):
        self.assertEqual(len(self.hotel.rooms), 3)
        self.assertEqual(self.hotel.rooms[0], self.room1)
        self.assertEqual(self.hotel.rooms[1], self.room2)
        self.assertEqual(self.hotel.rooms[2], self.room3)

    def test_search_availability(self):
        req = ReservationRequest(date(2024, 8, 28), date(2024, 8, 30), defaultdict(int, {RoomType.SINGLE: 1}))
        avail = self.hotel.search(req)
        self.assertEqual(avail[RoomType.SINGLE], 2)

    def test_reserve_room(self):
        req = ReservationRequest(date(2024, 8, 28), date(2024, 8, 30), defaultdict(int, {RoomType.SINGLE: 1, RoomType.DOUBLE: 1}))
        reservation = self.hotel.reserve(req)
        self.assertEqual(len(reservation.rooms), 2)
        self.assertEqual(self.hotel.history[self.room1], self.hotel.date_range(req.s, req.e))
        self.assertEqual(self.hotel.history[self.room2], self.hotel.date_range(req.s, req.e))

        # Check that rooms are no longer available for the same dates
        req2 = ReservationRequest(date(2024, 8, 28), date(2024, 8, 30), defaultdict(int, {RoomType.SINGLE: 1, RoomType.DOUBLE: 1}))
        avail = self.hotel.search(req2)
        self.assertEqual(avail[RoomType.SINGLE], 1)
        self.assertEqual(avail[RoomType.DOUBLE], 0)

    def test_reserve_not_enough_rooms(self):
        req = ReservationRequest(date(2024, 8, 28), date(2024, 8, 30), defaultdict(int, {RoomType.SINGLE: 3}))
        with self.assertRaises(NotEnoughRoomForReservationException):
            self.hotel.reserve(req)

    def test_cancel_reservation(self):
        req = ReservationRequest(date(2024, 8, 28), date(2024, 8, 30), defaultdict(int, {RoomType.SINGLE: 1, RoomType.DOUBLE: 1}))
        reservation = self.hotel.reserve(req)
        self.hotel.cancel(reservation)

        # Check that the rooms are now available again
        req2 = ReservationRequest(date(2024, 8, 28), date(2024, 8, 30), defaultdict(int, {RoomType.SINGLE: 2, RoomType.DOUBLE: 1}))
        avail = self.hotel.search(req2)
        self.assertEqual(avail[RoomType.SINGLE], 2)
        self.assertEqual(avail[RoomType.DOUBLE], 1)

if __name__ == '__main__':
    unittest.main()
