# simple factory, a class that has one creation method with a large conditional that based on method parameters chooses which product class to instantiate and then return
from enum import Enum
from typing import Dict

# 文件格式
class FileFormat(Enum): EPUB = 'EPUB'; PDF = 'PDF'; MOBI = 'MOBI'

# 图书
class Book:
    def __init__(self, name: str, format: FileFormat): self.name = name; self.format = format

# 阅读器基类
class Reader:
    def read(self, book: Book): raise NotImplementedError

# 各种格式的阅读器
class EPUBReader(Reader):
    def read(self, book: Book): print(f'Using EPUB reader, book content is: {book.name}')

class PDFReader(Reader):
    def read(self, book: Book): print(f'Using PDF reader, book content is: {book.name}')

class MOBIReader(Reader):
    def read(self, book: Book): print(f'Using MOBI reader, book content is: {book.name}')

# 阅读器工厂类
class ReaderFactory:
    def create_reader(self, format: FileFormat) -> Reader:
        if format == FileFormat.EPUB: return EPUBReader()
        elif format == FileFormat.PDF: return PDFReader()
        elif format == FileFormat.MOBI: return MOBIReader()
        else: raise ValueError("Unsupported format")

# Kindle 类，管理书籍和阅读
class Kindle:
    def __init__(self): self.book_name_to_book: Dict[str, Book] = {}; self.reader_factory = ReaderFactory()

    def readBook(self, book_name: str):
        if book_name not in self.book_name_to_book: print('Book does not exist'); return
        book = self.book_name_to_book[book_name]
        reader = self.reader_factory.create_reader(book.format)
        reader.read(book)

    def upload(self, book_name: str, book_format: FileFormat):
        if book_name in self.book_name_to_book: print('book alr exist'); return
        self.book_name_to_book[book_name] = Book(book_name, book_format)

    def delete(self, book_name: str):
        if book_name not in self.book_name_to_book: print('Book does not exist'); return
        del self.book_name_to_book[book_name]

# 测试用例
# 初始化 Kindle
kindle = Kindle()

# 上传书籍
kindle.upload('EPUBBook', FileFormat.EPUB)
kindle.upload('PDFBook', FileFormat.PDF)
kindle.upload('MOBIBook', FileFormat.MOBI)

# 测试读取功能
print("\n--- Test #1: Read EPUB Book ---")
kindle.readBook('EPUBBook')

print("\n--- Test #2: Read PDF Book ---")
kindle.readBook('PDFBook')

print("\n--- Test #3: Read MOBI Book ---")
kindle.readBook('MOBIBook')

# Edge Case: 尝试读取不存在的书籍
print("\n--- Test #4: Read Non-existent Book ---")
kindle.readBook('NonExistentBook')
