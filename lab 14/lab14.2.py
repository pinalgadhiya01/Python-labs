class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

    def discount(self, percent):
        self.price = self.price - (self.price * percent / 100)


# Creating two books
b1 = Book("The Alchemist", "Paulo Coelho", 500)
b2 = Book("Harry Potter", "J.K. Rowling", 800)

print("Before Discount:")
b1.show()
b2.show()

# Apply 10% discount to first book
b1.discount(10)

print("After 10% Discount on Book 1:")
b1.show()
