import mysql.connector


class DBUtils:
    def __init__(self):
        try:
            self.config_file = "my.conf"
            self.connex = mysql.connector.connect(option_files=self.config_file)

            if self.connex.is_connected():
                print("Connected")

            else:
                print("Not connected")

        except mysql.connector.Error as e:
            print(e)
            self.close()

    def execute_select_query(self, table_name, table_name2=None, param=None):
        return_set = []
        cursor = self.connex.cursor(dictionary=True)

        if param and table_name2 is None:
            cursor.execute("select * from {}".format(table_name))

        elif param is None:
            cursor.execute("select * from {} inner join {} on books.author_name = authors.author_name".format(table_name, table_name2))
        else:
            where_clause = 'WHERE ' + ' AND ' .join(['`' + k + '` = %s' for k in param.keys()])

            print(where_clause)
            values = list(param.values())
            sql = "select * from {} {}".format(table_name, where_clause)
            print(sql)
            cursor.execute(sql, values)

        for x in cursor:
            return_set.append(x)

        cursor.close()

        return return_set

    def execute_insert_record(self, book, author):
        cursor = self.connex.cursor(dictionary=True)
        add_record1 = "INSERT INTO books (isbn, title, author_name) VALUES(%s, %s, %s)"
        add_record2 = "INSERT INTO authors (author_name, age, nationality) VALUES(%s, %s, %s)"

        record1 = (book.isbn, book.title, book.author_name)
        record2 = (book.author_name, author.age, author.nationality)

        cursor.execute(add_record2, record2)
        cursor.execute(add_record1, record1)

        self.connex.commit()
        cursor.close()

        return "Database Successfully added a New Row!"
