# library_management.py

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available (not checked out)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and checks it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        print(f"Book '{title}' is not available for checkout.")
        return False

    def return_book(self, title):
        """Finds a book by title and returns it (makes it available)."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        print(f"Book '{title}' is not currently checked out.")
        return False

    def list_available_books(self):
        """Lists all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)

