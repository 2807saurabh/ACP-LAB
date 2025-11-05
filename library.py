class Book:
    def __init__(self, name):
        self.__name = name      
        self.__is_issued = False

    def get_name(self):
        return self.__name

    def issue(self):
        if not self.__is_issued:
            self.__is_issued = True
            return True
        return False

    def return_book(self):
        if self.__is_issued:
            self.__is_issued = False
            return True
        return False


class Member:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.issued_books = []

    def borrow(self, book):
        if len(self.issued_books) < self.limit and book.issue():
            self.issued_books.append(book)
            print(f"{self.name} borrowed {book.get_name()}")
        else:
            print(f"{self.name} cannot borrow {book.get_name()}")

    def return_book(self, book):
        if book in self.issued_books and book.return_book():
            self.issued_books.remove(book)
            print(f"{self.name} returned {book.get_name()}")


class StudentMember(Member):
    def __init__(self, name):
        super().__init__(name, limit=2)


class FacultyMember(Member):
    def __init__(self, name):
        super().__init__(name, limit=5)


books = [Book("Python"), Book("Java"), Book("C++")]

name = input("Enter your name: ")
type_mem = input("Are you Student or Faculty? ").lower()

if type_mem == "student":
    member = StudentMember(name)
else:
    member = FacultyMember(name)

member.borrow(books[0])
member.borrow(books[1])
member.borrow(books[2])  

member.return_book(books[0])
