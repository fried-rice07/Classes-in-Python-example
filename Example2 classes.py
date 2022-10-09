class Book:
    def __init__(self, Title, Author, Price):
        self.Title = Title
        self.Author = Author
        self.Price = Price
    def View(self):
        return 'Book Title: ' + self.Title + '\nAuthor: ' + self.Author + '\nPrice: ' + self.Price
x = Book('Life is Hard', 'Marcel James V. Aribal' , 'Php 100.00')
print(x.View())





