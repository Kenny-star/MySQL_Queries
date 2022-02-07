class Book:
    isbn = 0
    title = ""
    author_name = ""

    def __init__(self, isbn, title, author_name):
        self.isbn = isbn
        self.title = title
        self.author_name = author_name
