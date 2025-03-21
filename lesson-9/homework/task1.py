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
    
    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    MAX_BORROW_LIMIT = 3
    
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {self.MAX_BORROW_LIMIT} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
        else:
            raise BookNotFoundException(f"{self.name} did not borrow {book.title}.")
    
    def __str__(self):
        books = ', '.join([book.title for book in self.borrowed_books]) or "No books borrowed"
        return f"{self.name}: {books}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")
    
    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Member '{name}' added successfully!")
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(f"Book '{title}' not found in library.")
    
    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        raise ValueError(f"Member '{name}' not found.")
    
    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        try:
            member.borrow_book(book)
            print(f"{member_name} successfully borrowed '{book_title}'.")
        except (BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)
    
    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        try:
            member.return_book(book)
            print(f"{member_name} successfully returned '{book_title}'.")
        except BookNotFoundException as e:
            print(e)
    
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)
    
    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            print(member)


if __name__ == "__main__":
    library = Library()
    
    
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    
    
    library.add_member("Alice")
    library.add_member("Bob")
    
    
    library.borrow_book("Alice", "1984")
    library.borrow_book("Bob", "To Kill a Mockingbird")
    
    
    library.display_books()
    library.display_members()
    

    library.return_book("Alice", "1984")
    library.return_book("Bob", "To Kill a Mockingbird")
    
  
    library.display_books()
    library.display_members()
