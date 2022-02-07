class Author:
    author_name = ""
    age = 0
    nationality = ""

    def __init__(self, author_name, age, nationality):
        self.author_name = author_name
        self.age = age
        self.nationality = nationality

    def __init__(self, age, nationality):
        self.age = age
        self.nationality = nationality
