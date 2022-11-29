
class Book: # its a convention to keep the first letter capital for classes!
  def __init__(self, title, quantity, author, price):
    self.title = title
    self.quantity = quantity
    self.author = author
    self.price = price

  def __repr__(self) -> str:
    return f"Book : {self.title}, Quantity : {self.quantity}, Author : {self.author}, , Price : {self.price}"

  def stringify(self):
    print("Book : {self.title}, Quantity : {self.quantity}, \nAuthor : {self.author}, \nPrice : {self.price}")  
