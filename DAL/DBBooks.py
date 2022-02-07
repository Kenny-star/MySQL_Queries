from DAL.DBUtils import DBUtils
from Entities import Author, Book


class DBBooks:
    dtu = DBUtils()

    def select_all_books(self):
        return self.dtu.execute_select_query("books", "authors")

    def select_book(self, isbn: int):
        return self.dtu.execute_select_query("books", param={'isbn': isbn})

    def insert_record(self, b: Book, a: Author):
        return self.dtu.execute_insert_record(b, a)
