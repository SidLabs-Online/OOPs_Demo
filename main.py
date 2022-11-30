#1 classes
# import books

# book1 = books.Book("Harry Potter", 15, "lance",100 )
# book2 = books.Book("5 habits", 29, "Stephen Kovi",200 )

# print(book1.stringify)
# print(book2.stringify)

# print(type(book1))
# print(type(book2))

#2 Encapsulation
# import encapsulation as en

# book1 = en.Book("Harry Potter", 15, "lance",100 )

# book2 = en.Book("5 habits", 29, "Stephen Kovi",200 )

# # print(book1.title)
# # print(book2.title)
# # print(book1.__discount)

# book1.set_discount(0.20)
# print("The new price of the book", book1.title, "is :$", book1.get_price())

#3 Inheritance
# import inheritance as inh

# novel1 = inh.Novel("green mountains",10, "Lance", 100, "Adventure", 300)

# novel2 = inh.Novel("green plains",5, "Sid", 2, "Adventure", 20)

# novel1.stringify()
# novel2.stringify()

#4. 'Polymorphism' 
# comes from the Greek language and means 'something that takes on multiple forms.'

# import polymorphism as poly

# novel1 = poly.Novel('Ginger Sky', 20, "Tom Hanks", 37, 'self help', 204)

# acad1 = poly.Academic("Python Mastery", 12, "sid", 11, "Computer Science" )

# print(novel1)
# print(acad1)

#5. Abstraction
# import abstraction as abs

# novel1 = abs.Novel('Ginger Sky', 20, "Tom Hanks", 37, 'self help', 204)

# academic1 = abs.Academic("Python Mastery", 12, "sid", 11, "Computer Science" )

# print(novel1)
# print(academic1)

#6. Method Overloading
import methodOverloading as mo


Paobj1 = mo.Parent()
Paobj1.call_me()

Cobj1 = mo.Child()
Cobj1.call_me()







