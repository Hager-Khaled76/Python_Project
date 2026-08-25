# Task 4: Library Borrowing System
#------------------------------------
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # starts as available


class Member:

    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.borrowed = []  # Composition

    def borrow(self, book):
        if not book.available:
            return "Not available"

        if len(self.borrowed) >= self.limit:
            return "Limit reached"

        book.available = False
        self.borrowed.append(book)
        return "OK"

    def return_book(self, title):
        for book in self.borrowed:
            if book.title == title:
                book.available = True
                self.borrowed.remove(book)
                return "Returned"

        return "Not found"


if __name__ == '__main__':

    b1 = Book("Python", "Ali")
    b2 = Book("Java", "Sara")
    b3 = Book("DB", "Omar")

    m = Member("Ahmed", 2)

    print("Borrow Python:", m.borrow(b1))
    print("Borrow Java:", m.borrow(b2))
    print("Borrow DB:", m.borrow(b3))
    print("Return Python:", m.return_book("Python"))
    print("Borrow DB:", m.borrow(b3))

    print(f"{m.name} has {len(m.borrowed)} books")