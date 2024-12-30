class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "available"

    def borrow(self):
        if self.status == "available":
            self.status = "borrowed"
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

    def return_book(self):
        self.status = "available"
        print(f"{self.title} has been returned.")

#--------------------------------------------------------------

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.status == "available":
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} did not borrow {book.title}.")
#---------------------------------------------------------------

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member registered: {member.name}")

    def lend_book(self, member, book_id):
        for book in self.books:
            if book.book_id == book_id:
                member.borrow_book(book)
                return
        print("Book not found.")

    def receive_return(self, member, book_id):
        print("Thanks for using our library")
        for book in self.books:
            if book.book_id == book_id:
                member.return_book(book)
                return
        
        print("Book not found.")

#=====================================================
"""main file to extract class, its attributes, and behaviiour"""

if __name__ == "__main__":
    library = Library()

    library.add_book(Book(1, "wheels and wings", "KCG"))
    library.add_book(Book(2, "pysio of money", "hoswell"))
    library.add_book(Book(3, "data analysis using python", "mckinney"))
    print()

    member1 = Member(101, "Rahul")
    member2 = Member(102, "shakeel")
    print()

    library.register_member(member1)
    library.register_member(member2)
    print()

    library.lend_book(member1, 1)
    library.lend_book(member1, 2)
    print()

    library.receive_return(member1, 1)
    
