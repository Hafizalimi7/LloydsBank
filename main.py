class LloydsBank:
  def __init__(self, f_name, l_name, age):
    self.f_name = f_name
    self.l_name = l_name
    self.age = age
  
  def first_name(self):
    return self.f_name
  
  def last_name(self):
    return self.l_name
  
  def p_age(self):
    return self.age
  
  
class BankAcc(LloydsBank):
  def __init__(self, f_name, l_name, age, func, wage):
    super().__init__(f_name, l_name, age)
    self.func = func
    self.balance = 1000
    self.wage = wage
    self.monthly_wage = 0
    self.year_wage = 0
  
  def end_of_month_salary(self):
    self.monthly_wage = int(self.wage * 4)
    return self.monthly_wage
  
  def yearly_salary(self):
    self.year_wage = int(self.monthly_wage * 12)
    return self.year_wage

class SecureUnit(BankAcc, LloydsBank):
  def __init__(self, f_name, l_name, age, func, wage, password, secrurity_keyword):
    super().__init__(f_name, l_name, age, func, wage)
    self.password = password
    self.security_keyword = secrurity_keyword
  
  def __call__(self, *args):
    print(f"Hello {self.f_name} {self.l_name}, Welcome to Loyds Bank. Can you type in your password?")
    print(SecureUnit.checking_correct_password(self))
    return self.func(*args)
  
  def checking_correct_password(self):
    user_input = input("Type In Your Password: ")
    if user_input != self.password:
      user_security = input("Type In Your Secruity: ")
      if user_security != self.security_keyword:
        print("Your account is blocked, please contact the bank")
      else:
        user_input = input("Type In Your Password: ")
    else:
      SecureUnit.your_account(self)
  
  def your_account(self):
    print(f"Hi {self.f_name }, What would you like ?")
    user1_input = input("")
    if user1_input == "check balance":
      print("No problem I'll get that sorted for you")
      print(f"Your balance is {self.balance}")
      print(f"{self.f_name }, is there anything else you like help with ?")
      user1_input = input("")
      if user1_input == "no":
        print("Thnak you good bye")
      else:
        print("How can i help?")

def intro(self):
  return self

@SecureUnit(f_name="Mike", l_name="Jones", age=24, password="Yes", secrurity_keyword="pop", func=intro, wage=400)
def user1():
  pass

# deposit()

# user = SecureUnit("Josh", "Palley", 34, "Kizzy", "Mother")
# user.checking_correct_password()
    
"""year salary"""
# def user3():
#   Josh  = BankAcc("Josh", "Palley", 34, None, 1000)
#   Josh.end_of_month_salary()
#   print(Josh.yearly_salary())
# user3()

"""monthly wage"""
# def user1():
#   Tom = BankAcc("mike","tom",23,None,2000)
#   wage = Tom.end_of_month_salary
#   print(f"{Tom.f_name} earns {wage()} ")
# user1()




