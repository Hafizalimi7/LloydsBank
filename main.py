from typing import Any


class LloydsBank:
  def __init__(self, f_name, l_name, age):
    self.f_name = f_name
    self.l_name = l_name
    self.age = age
  
  def Bank_name(self):
    print("LloydsBank")
  
  def first_name(self):
    return self.f_name
  
  def last_name(self):
    return self.l_name
  
  def p_age(self):
    return self.age
  
class BankAcc(LloydsBank):
  def __init__(self, f_name, l_name, age, func):
    super().__init__(f_name, l_name, age)
    self.func = func
    
  
  def __call__(self, *args):
    print(f"Hello {self.f_name} {self.l_name}, Welcome to Loyds Bank. How can i help you ?")
    return self.func(*args)

def intro(self):
  return self

@BankAcc(f_name="Mike", l_name="Jones", age=24, func=intro)
def welcome():
  print("Byee")

print(welcome())