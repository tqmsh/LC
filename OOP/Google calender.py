from threading import Lock
from datetime import datetime
from typing import List

class Event:
    def __init__(self, type: str, st: datetime, et: datetime):
        self.type: str = type
        self.st: datetime = st
        self.et: datetime = et

    def conflicts_with(self, other: 'Event') -> bool:
        return not (self.et <= other.st or other.et <= self.st)


class Reminder(Event):
    def __init__(self, st: datetime, et: datetime, note: str):
        super().__init__("Reminder", st, et)
        self.note: str = note

    def __repr__(self):
        return f"Reminder(note={self.note})"

class Calendar:
    def __init__(self):
        self.events: List[Event] = []
        self.lock: Lock = Lock()

    def add_event(self, event: Event):
        with self.lock:
            for e in self.events:
                if event.conflicts_with(e):
                    raise ValueError("Event conflicts with existing event")
            if event.et <= event.st:
                raise ValueError("End time must be after start time")
            self.events.append(event)

    def list_events(self) -> List[Event]:
        return self.events

class User:
    def __init__(self, name: str, occupation: str, email: str, contact: str):
        self.name: str = name
        self.occupation: str = occupation
        self.email: str = email
        self.contact: str = contact
        self.calendar: Calendar = Calendar()

    def __repr__(self):
        return f"User(name={self.name}, occupation={self.occupation})"

class Meeting(Event):
    def __init__(self, st: datetime, et: datetime, agenda: str, participants: List[User]):
        super().__init__("Meeting", st, et)
        self.agenda: str = agenda
        self.participants: List[User] = participants

    def add_participants(self, new_participants: List[User]):
        self.participants.extend(new_participants)
    
    def list_participants(self) -> List[str]:
        return self.participants

    def __repr__(self):
        return f"Meeting(agenda={self.agenda}, participants={self.participants})"

Alice = User(name="Alice", occupation="Engineer", email="alice@example.com", contact="123-456-7890")
Bob = User(name="Bob", occupation="Engineer", email="bob@example.com", contact="123-456-7890")

start_time1 = datetime(2024, 9, 18, 10, 0)
end_time1 = datetime(2024, 9, 18, 11, 0)
meeting = Meeting(st=start_time1, et=end_time1, agenda="Team Sync", participants=[Alice, Bob])
Alice.calendar.add_event(meeting)
print("Test #1 passed - Meeting added:", meeting)

start_time2 = datetime(2024, 9, 18, 10, 30)   
end_time2 = datetime(2024, 9, 18, 11, 30)
try:
    conflicting_meeting = Meeting(st=start_time2, et=end_time2, agenda="Client Call", participants=[Alice, Bob])
    Alice.calendar.add_event(conflicting_meeting)
except ValueError as e:
    print("Test #2 passed - Conflict detected:", e)

start_time3 = datetime(2024, 9, 18, 11, 30)
end_time3 = datetime(2024, 9, 18, 12, 0)
reminder = Reminder(st=start_time3, et=end_time3, note="Buy groceries")
Bob.calendar.add_event(reminder)
print("Test #3 passed - Reminder added:", reminder)

try:
    invalid_event = Meeting(st=datetime(2024, 9, 18, 12, 0), et=datetime(2024, 9, 18, 11, 0), agenda="Invalid Meeting", participants=[Alice])
    Alice.calendar.add_event(invalid_event)
except ValueError as e:
    print("Test #4 passed - Edge case (invalid event time) detected:", e)

print("Test #5 - Participants in the first meeting:")
print(meeting.list_participants()) 