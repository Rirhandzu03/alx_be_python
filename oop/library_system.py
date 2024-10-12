class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
         
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Implementing a Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []  # List to store book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)


# Example usage to match expected output
library = Library()

# Adding books to the library
library.add_book(PrintBook("Pride and Prejudice", "Jane Austen", 300))
library.add_book(EBook("Snow Crash", "Neal Stephenson", 500))
library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))

# Listing books in the library
library.list_books()


          
        