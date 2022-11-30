# super class
class Book: # its a convention to keep the first letter capital for classes!
  def __init__(self, title, quantity, author, price):
    self.title = title
    self.quantity = quantity
    self.author = author
    self.price = price

  def __repr__(self) -> str:
    return f"Book : {self.title}, Quantity : {self.quantity}, Author : {self.author}, , Price : {self.price}"

class Novel(Book): # Child class or a sub class
  def __init__(self, title, quantity, author, price, genre, pages):
    super().__init__(title, quantity, author, price)
    self.genre = genre
    self.pages = pages

  

class Academic(Book):  # Child class or a sub class
  def __init__(self, title, quantity, author, price, subject):
    super().__init__(title, quantity, author, price)
    self.subject = subject

  def __repr__(self) -> str:
    return f"Book : {self.title}, Quantity : {self.quantity},Author : {self.author},Price : {self.price}, Subject : {self.subject}"
