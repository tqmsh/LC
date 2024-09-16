from datetime import datetime
from typing import List, Optional

# Define the classes
class BookStatus:
    AVAILABLE, RESERVED, LOANED, LOST = "Available", "Reserved", "Loaned", "Lost"

class ReservationStatus:
    WAITING, PENDING, COMPLETED, CANCELED = "Waiting", "Pending", "Completed", "Canceled"

class BookFormat:
    HARDCOVER, AUDIOBOOK, EBOOK, NEWSPAPER, MAGAZINE, JOURNAL = "Hardcover", "Audiobook", "Ebook", "Newspaper", "Magazine", "Journal"

class Book:
    def __init__(self, ISBN: str, title: str, author: str, subject: str, publisher: str, publish_date: datetime, language: str, numOfPages: int):
        self.ISBN, self.title, self.author, self.subject, self.publisher, self.publish_date, self.language, self.numOfPages = ISBN, title, author, subject, publisher, publish_date, language, numOfPages
        self.book_items: List['BookItem'] = []

class BookItem:
    def __init__(self, barcode: str, borrowed: Optional[datetime] = None, dueDate: Optional[datetime] = None, price: float = 0.0, 
                 format: BookFormat = BookFormat.HARDCOVER, status: BookStatus = BookStatus.AVAILABLE, borrower_id: Optional[str] = None):
        self.barcode, self.borrowed, self.dueDate, self.price, self.format, self.status, self.borrower_id = barcode, borrowed, dueDate, price, format, status, borrower_id

    def checkout(self):
        self.status, self.borrowed = BookStatus.LOANED, datetime.now()

class Member:
    def __init__(self, member_id: str, dateOfMembership: datetime, password: str, email: str, address: str):
        self.member_id, self.dateOfMembership, self.password, self.email, self.address = member_id, dateOfMembership, password, email, address
        self.reservations: List['Reservation'] = []
        self.books: List[BookItem] = []

    def get_total_checked_out_books(self) -> int:
        return len(self.books)

class Reservation:
    def __init__(self, creationDate: datetime, book_item: BookItem, status: ReservationStatus = ReservationStatus.WAITING):
        self.creationDate, self.book_item, self.status = creationDate, book_item, status

class Param:
    def __init__(self, title: str, author: str, subject: str, publication_date: datetime):
        self.title, self.author, self.subject, self.publication_date = title, author, subject, publication_date

class Fine:
    def __init__(self, amount: float):
        self.amount = amount

class Specification:
    def is_satisfied(self, param: Param, book: Book) -> bool:
        pass

class TitleSpecification(Specification):
    def is_satisfied(self, param: Param, book: Book) -> bool:
        return param.title == book.title

class AndSpecification(Specification):
    def __init__(self, spec_one: Specification, spec_other: Specification):
        self.spec_one, self.spec_other = spec_one, spec_other

    def is_satisfied(self, param: Param, book: Book) -> bool:
        return self.spec_one.is_satisfied(param, book) and self.spec_other.is_satisfied(param, book)

class Notification:
    def __init__(self, notification_id: int, creation_date: datetime, content: str):
        self.notification_id, self.creation_date, self.content = notification_id, creation_date, content

    def send_notification(self):
        pass

class PostalNotification(Notification):
    def __init__(self, notification_id: int, creation_date: datetime, content: str, address: str):
        super().__init__(notification_id, creation_date, content)
        self.address = address

    def send_notification(self):
        print(f"Postal notification sent to {self.address}")

class EmailNotification(Notification):
    def __init__(self, notification_id: int, creation_date: datetime, content: str, email: str):
        super().__init__(notification_id, creation_date, content)
        self.email = email 

    def send_notification(self):
        print(f"Email notification sent to {self.email}")

class Transaction:
    def __init__(self, created_on: datetime, amount: float):
        self.created_on, self.amount = created_on, amount       

class CreditCardTransaction(Transaction): 
    def __init__(self, created_on: datetime, amount: float, name_on_card: str, card_number: str, expiry: datetime, pin: int):
        super().__init__(created_on, amount)
        self.name_on_card, self.card_number, self.expiry, self.pin = name_on_card, card_number, expiry, pin

class LibraryManagementSystem:
    def __init__(self):
        self.books: List[Book] = []
        self.book_items: List[BookItem] = []
        self.members: List[Member] = []
        self.reservations: List[Reservation] = []

    def make_reservation(self, book_item: BookItem, member: Member):
        reservation = Reservation(datetime.now(), book_item)
        member.reservations.append(reservation)
        self.reservations.append(reservation)

    def search(self, param: Param, spec: Specification) -> Optional[Book]:
        return next((book for book in self.books if spec.is_satisfied(param, book)), None)

    def send_notification(self, notification: Notification, member: Member):
        notification.send_notification()

    def checkout(self, book_item: BookItem, member: Member):
        member.books.append(book_item)
        book_item.checkout()

    def fine_member(self, book_item: BookItem, fine: Fine):
        print(f"Fine imposed: ${fine.amount} for book {book_item.barcode}")

    def make_payment(self, fine: Fine, transaction: Transaction):
        print(f"Payment of ${fine.amount} made successfully on {transaction.created_on}")

# Tests
def test_book_creation():
    book = Book("123", "Book Title 1", "Author A", "Subject A", "Publisher A", datetime.now(), "English", 200)
    assert book.ISBN == "123"
    assert book.title == "Book Title 1"

def test_book_item_creation():
    book_item = BookItem("barcode1", price=25.0, format=BookFormat.HARDCOVER)
    assert book_item.barcode == "barcode1"
    assert book_item.price == 25.0

def test_make_reservation():
    library = LibraryManagementSystem()
    book = Book("123", "Book Title 1", "Author A", "Subject A", "Publisher A", datetime.now(), "English", 200)
    book_item = BookItem("barcode1", price=25.0, format=BookFormat.HARDCOVER)
    member = Member("1", datetime.now(), "password123", "john.doe@example.com", "123 Main St")
    library.books.append(book)
    library.book_items.append(book_item)
    library.members.append(member)
    library.make_reservation(book_item, member)
    assert len(member.reservations) == 1
    assert len(library.reservations) == 1

def test_checkout():
    library = LibraryManagementSystem()
    book = Book("123", "Book Title 1", "Author A", "Subject A", "Publisher A", datetime.now(), "English", 200)
    book_item = BookItem("barcode1", price=25.0, format=BookFormat.HARDCOVER)
    member = Member("1", datetime.now(), "password123", "john.doe@example.com", "123 Main St")
    library.books.append(book)
    library.book_items.append(book_item)
    library.members.append(member)
    library.checkout(book_item, member)
    assert book_item.status == BookStatus.LOANED
    assert len(member.books) == 1

def test_fine_member():
    library = LibraryManagementSystem()
    book_item = BookItem("barcode1", price=25.0, format=BookFormat.HARDCOVER)
    fine = Fine(5.0)
    library.fine_member(book_item, fine)

def test_make_payment():
    library = LibraryManagementSystem()
    fine = Fine(5.0)
    transaction = CreditCardTransaction(datetime.now(), 5.0, "John Doe", "1234567890123456", datetime(2025, 1, 1), 1234)
    library.make_payment(fine, transaction)

def test_send_notification():
    library = LibraryManagementSystem()
    member = Member("1", datetime.now(), "password123", "john.doe@example.com", "123 Main St")
    email_notification = EmailNotification(1, datetime.now(), "Your reservation is available", "john.doe@example.com")
    library.send_notification(email_notification, member)

def test_search():
    library = LibraryManagementSystem()
    
    # Create a Book and BookItem
    book = Book("123", "Book Title 1", "Author A", "Subject A", "Publisher A", datetime.now(), "English", 200)
    book_item = BookItem("barcode1", price=25.0, format=BookFormat.HARDCOVER)
    
    # Associate the BookItem with the Book
    book.book_items.append(book_item)
    
    # Add the Book and BookItem to the library
    library.books.append(book)
    library.book_items.append(book_item)
    
    # Define the search specification and parameters
    spec = TitleSpecification()
    param = Param("Book Title 1", "Author A", "Subject A", datetime.now())
    
    # Perform the search
    result = library.search(param, spec)
    
    # Assert the search result
    assert result is not None
    assert result.title == "Book Title 1"


if __name__ == "__main__":
    test_book_creation()
    test_book_item_creation()
    test_make_reservation()
    test_checkout()
    test_fine_member()
    test_make_payment()
    test_send_notification()
    test_search()
    print("All tests passed!")