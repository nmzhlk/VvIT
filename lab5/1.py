class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f'Название книги: «{self.title}», Автор: {self.author}, Год издания: {self.year}'


book1 = Book('Капитанская дочка', 'Александр Пушкин', 1836)
book2 = Book('Война и мир', 'Лев Толстой', 1869)

print(book1.get_info())
print(book2.get_info())
