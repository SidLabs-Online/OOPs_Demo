# Encapsulation is the process of preventing clients from 
# accessing certain properties, which can only be accessed through specific methods.

# Private attributes are inaccessible attributes, and 
# information hiding is the process of making particular attributes private. 

class Book: # its a convention to keep the first letter capital for classes!
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

