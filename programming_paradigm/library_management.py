# library_management.py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list of books
        self.checked_out_books = set()  # Track checked-out books

    def add_book(self, book):
        self.books.append(book)

    def list_available_books(self):
        available_books = [book for book in self.books if book.title not in self.checked_out_books]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and title not in self.checked_out_books:
                self.checked_out_books.add(title)
                print(f"Checked out: {book}")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        if title in self.checked_out_books:
            self.checked_out_books.remove(title)
            print(f"Returned: {title}")
        else:
            print(f"Book '{title}' was not checked out.")
