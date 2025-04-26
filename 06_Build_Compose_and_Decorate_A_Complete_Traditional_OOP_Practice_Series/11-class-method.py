class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def show_total_books(cls):
        print("Total books added:", cls.total_books)

# Example usage
book1 = Book("The Alchemist")
book2 = Book("1984")
book3 = Book("To Kill a Mockingbird")

Book.show_total_books()
