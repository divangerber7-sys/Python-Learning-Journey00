# Aggregation = Represents a relationship where one object (the whole)
#               contains references to one or more INDEPENDENT objects (the parts).
#               The parts can exist without the whole.

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


if __name__ == "__main__":
    library = Library("The Alone Times")

    book1 = Book("The Way of Zen", "Alan Watts")
    book2 = Book("The Wisdom of Insecurity", "Alan Watts")
    book3 = Book("The Spirit of Zen", "Alan Watts")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print(library.name)

    for book in library.list_books():
        print(book)
