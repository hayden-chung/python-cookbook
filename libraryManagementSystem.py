'''
1. Should be able to search by title, author, subject category, publication date. 
--> [title, author, subject category, publication date]

2. Unique ID no., rack number



Librarian: add & modify books, boook items, and users
Member: can search the catalog, check-out, reserve, renew, and return a book
System: send notifications for overdue books, canceled reserverations

'''

# book1 = Book(title, author, subjec category, publication date, stock)


class User:
    def __init__ (self, username):
        self.username = username
        self.my_books = []

    def my_info(self):
        print(f'Name: {self.username}')

    def borrow(self, book):
        if book.stock > 0: 
            book.borrow_book()
        

class Book:
    def __init__(self, book_name, stock):
        self.bookname = book_name
        self.stock = stock

    def borrow_book(self):
        self.stock -= 1
        print('stock: {self.stock}')

book1 = Book('book1', 4)

person1 = User('person1')
person1.my_info()

person1.borrow(book1)






