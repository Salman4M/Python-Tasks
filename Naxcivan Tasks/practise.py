class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

#if we use string method (__str__) our objects has to be string. For example When we create object of
#Book class and want to show it in the console it will show us place of the object in the python memory.
#[<__main__.Book object at 0x000001F0691C0190>] Because it's not string.To make the object string 
# we have to use str() method to see return of __str__ method.Also we can call atribute of object to 
# make it string: book.author . If we use str() for the object itself (str(book)) it will the return
# result of __str__ method. But if we call the attribute of the object to convert it to str , __str__
#method won't work. In this time we will see what we set in the return of the method (probably attribute of object).

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Added '{book.title}' to the library."

    def display_available_books(self):
        if self.books:
            available_books = [str(book) for book in self.books if book.available]
            if available_books:
                return "Available Books:\n"+"\n".join(available_books)
            else:
                return "No books available in the library."
        else:
            return "No books available in the library."

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return f"Borrowed '{book.title}' from the library."
        return f"Book '{title}' is either unavailable or does not exist in the library."


    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                return f"Returned '{book.title}' to the library."
        return f"Book '{title}' was not borrowed or does not exist in the library."


    def display_borrowed_books(self):
        borrowed_books = [str(book) for book in self.books if not book.available]
        if borrowed_books:
            return "Borrowed Books:\n"+"\n".join(borrowed_books)
        else:
            return "No books are currently borrowed."


library = Library()

# Adding books to the library
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# # # Display available books
print(library.display_available_books())

# # # Borrow a book
# print(library.borrow_book("Harry Potter and the Philosopher's Stone"))
# print(library.borrow_book("To Kill a Mockingbird"))

# print(library.borrow_book("Homo Sapiens"))


# # # # Display borrowed books
# print(library.display_borrowed_books())

# # # # Return a borrowed book
# print(library.return_book("Harry Potter and the Philosopher's Stone"))
