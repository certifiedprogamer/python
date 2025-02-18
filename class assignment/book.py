class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"


book = Book("1984", "George Orwell", 328)
print(book)
