from DAL.DBBooks import DBBooks
from Entities.Author import Author
from Entities.Book import Book

books = DBBooks()
book = Book(32221111, "Hamlet", "William Shakespeare")
author = Author(70, "English")

books_list = books.select_all_books()
book_two = books.select_book(1)
insert_record = books.insert_record(book, author)

print(books_list)
print(book_two)
print(insert_record)

