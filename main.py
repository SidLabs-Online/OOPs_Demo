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
import inheritance as inh

novel1 = inh.Novel("green mountains",10, "Lance", 100, "Adventure", 300)

novel2 = inh.Novel("green plains",5, "Sid", 2, "Adventure", 20)

novel1.stringify()
novel2.stringify()






