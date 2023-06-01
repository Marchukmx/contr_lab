#3 part 2

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        print("Назва книги:", self.title)
        print("Автор:", self.author)

book1 = Book("Война и Мир", "Лев Тостой")
book1.get_info()

book2 = Book("Пайтон це легко", "Дмитро Кучинський")
book2.get_info()
