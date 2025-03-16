
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    MAX_BORROWED_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  

    def borrow_book(self, book, library):
        if book not in library.books:
            raise BookNotFoundException(f"Book '{book.title}' not found in the library.")

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{book.title}' is already borrowed.")

        if len(self.borrowed_books) >= self.MAX_BORROWED_BOOKS:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {self.MAX_BORROWED_BOOKS} books.")

     
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")


class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        print("Available Books in Library:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"- {book.title} by {book.author} [{status}]")

library = Library()


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


member1 = Member("Alice")

library.display_books()


try:
    member1.borrow_book(book1, library)
    member1.borrow_book(book2, library)
    member1.borrow_book(book3, library)
except Exception as e:
    print(e)


library.display_books()


try:
    extra_book = Book("Moby Dick", "Herman Melville")
    library.add_book(extra_book)  # Add it to library first
    member1.borrow_book(extra_book, library)
except Exception as e:
    print(e)


member1.return_book(book2)


library.display_books()
