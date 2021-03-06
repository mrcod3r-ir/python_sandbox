# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Define Class
class User:
  
  # Constructor
  
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age= age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1

# Init user object

brad = User('brad traversy', 'brad@gmail.com', 37)

brad.has_birthday()
print(brad.greeting())

# Extend class

class Customer(User):
  # Constructor
  # def __init__(self, name, email, age):
  #   self.name = name
  #   self.email = email
  #   self.age= age
  #   self.balance = 0
  
  def set_balance(self, balance):
    self.balance = balance

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init customer object
janet = Customer('Janet Johnson','janet@gmail.com',25)
janet.set_balance(500)

print(janet.greeting())

# Use parent and super 

class Client(User):
  def __init__(self, name, email, age,billAmount):
      super().__init__(name, email, age)
      self.billAmount = billAmount
      print(f'my bill amount is {billAmount}')
      


tom = Client('tomy','tomy@gmail.com',40,201)
print(tom.greeting())