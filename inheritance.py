# its a class's ability to inherit methods and characteristics from another class
# Subclass : or a child class : is the class that inherits
# Parent Class : Super Class : is the class from which the child inherits

class Book: # Parent class or a super class
  def __init__(self, title, quantity, author, price):
    self.title = title
    self.quantity = quantity
    self.author = author
    self.price = price
    self.__discount = None

  def set_discount(self, discount):# specific method to access the hidden attribute
    self.__discount = discount 

  def get_price(self):
    if self.__discount :
      return self.price * (1-self.__discount)
    else:
      return self.price


  
  def stringify(self):
    print("Book : {self.title}, Quantity : {self.quantity}, \nAuthor : {self.author}, \nPrice : {self.price}")  


class Novel(Book): # Child class or a sub class
  def __init__(self, title, quantity, author, price, genre, pages):
    super().__init__(title, quantity, author, price)
    self.genre = genre
    self.pages = pages

  def stringify(self):
    print("-------------------")
    print("Novel :", self.title, "\nQuantity :", self.quantity
          ,"\nAuthor :", self.author, "\n Price :$", self.price
          ,"\nGenre :", self.genre, "\nPages : ", self.pages )

class Academic(Book):  # Child class or a sub class
  def __init__(self, title, quantity, author, price, subject):
    super().__init__(title, quantity, author, price)
    self.subject = subject
  
  
