# Создайте класс с названием Book.
# Добавьте атрибуты: title, author, и pages.
# Создайте метод description(), который возвращает строку с описанием книги в 
# формате: "Название книги", написанная "Автор", содержит "Количество страниц" страниц.
# Создайте несколько объектов этого класса и вызовите метод description() для каждого объекта.

class book:
  def __init__(self,title, author,pages ) :
    self.title = title
    self.author = author
    self.pages = pages
      
  def description(self):
    return f'{self.title} написанная {self.author} содержит {self.pages} страниц.'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_all_books(self):
        return self.books


book1 = book(title= "harry potter", author=" j.rolling", pages= 1000)
book2 = book(title= "harry potter filosofer stone", author= "j.rolling", pages= 1030)

my_library = Library()

my_library.add_book(book1)
my_library.add_book(book2)
for book_in_library in my_library.get_all_books():
    print(book_in_library.description())
print(book1.description())
