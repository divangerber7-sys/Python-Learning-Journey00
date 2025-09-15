# Magic methods = "Dunder" methods (double underscores)
#                 Examples: __init__, __str__, __eq__, etc.
#                 They let you define/customize how objects behave
#                 with Python's built-in operators and functions.


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword.lower() in self.title.lower() or keyword.lower() in self.author.lower()

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' not found"


if __name__ == "__main__":
    book1 = Book("The Way of Zen", "Alan Watts", 256)
    book2 = Book("The Wisdom of Insecurity", "Alan Watts", 160)
    book3 = Book("Become What You Are", "Alan Watts", 144)

    # __str__
    print(book1)  # "The Way of Zen by Alan Watts"

    # __eq__, __lt__, __gt__
    print(book1 == book2)
    print(book1 < book3)
    print(book1 > book3)

    # __add__
    print(book2 + book3)  # total pages

    # __contains__
    print("zen" in book1)
    print("watts" in book3)

    # __getitem__
    print(book1["title"])
    print(book2["author"])
    print(book3["num_pages"])
    print(book1["audio"])  # invalid key
