class Book:
    def __init__(self, title, author, isbn, publication_year):
        # Store values as instance attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2026
        return current_year - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


# Example usage
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)

print(book1.get_summary())
print("Book age:", book1.get_age(), "years")