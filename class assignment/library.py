class Book:
    def __init__(self, title: str, author: str, isbn,):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        self.checked_out = True

    def return_book(self):
        self.checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"


class Member:
    def __init__(self, name: str, member_id: int):
        self.name = name
        self.member_id = member_id
        self.books_checked_out = list()

    def borrow_book(self, book: Book):
        if book.checked_out == False:
            print(f"{self.name} borrows {book.title}")
            self.books_checked_out.append(book)
            book.check_out()
            print("")

    def return_book(self, book: Book):
        if book.checked_out == True and book in self.books_checked_out:
            print(f"{self.name} returns {book.title}")
            self.books_checked_out.remove(book)
            book.return_book()
            print("")

    def list_books(self):
        print("Books:")
        for i in self.books_checked_out:
            print(i.title)
        print("")


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = list()

    def add_book(self, book: Book):
        self.books.append(book)

    def list_available_books(self):
        print("Available books:")
        for i in self.books:
            if i.checked_out == False:
                print(
                    f"{i} - Available")
        print("")

    def find_book_by_title(self, title):
        for i in self.books:
            if i.title == title:
                return i
        return None


libraby = Library("Libraby")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 3)
book2 = Book("1984", "George Orwell", 2)
book3 = Book("Dune", "Frank Herbert", 1)

libraby.add_book(book1)
libraby.add_book(book2)
libraby.add_book(book3)

joe = Member("joe", 2)

libraby.list_available_books()

book_ = libraby.find_book_by_title("The Hobbit")

joe.borrow_book(book_)

libraby.list_available_books()

joe.return_book(joe.books_checked_out[0])

libraby.list_available_books()