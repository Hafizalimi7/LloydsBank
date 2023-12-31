class LloydsBank:
  balance = 1000

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
    self.wage = wage
    self.monthly_wage = 0
    self.year_wage = 0
  
  def end_of_month_salary(self):
    self.monthly_wage = int(self.wage * 4)
    return self.monthly_wage
  
  def yearly_salary(self):
    self.year_wage = int(self.monthly_wage * 12)
    return self.year_wage

class PasswordCheck(BankAcc, LloydsBank):
  def __init__(self, f_name, l_name, func,  password, secrurity_keyword):
    super().__init__(f_name, l_name, func)
    self.password = password
    self.security_keyword = secrurity_keyword
  
  def __call__(self, *args):
    print(f"Hello {self.f_name} {self.l_name}, Welcome to Loyds Bank. Can you type in your password?")
    print(PasswordCheck.checking_correct_password(self))
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
      PasswordCheck.your_account(self)
 
class Services(PasswordCheck):
  def __init__(self, f_name ,withdraw, deposit, func):
    self.f_name = f_name
    self.withdraw = withdraw
    self.deposit = deposit
    self.func = func

  def __call__(self, *args):
    print(Services.your_account(self))
    return self.func(*args)
  
  def money_out(self):
    self.balance = self.balance - self.withdraw
    return self.balance
  
  def money_in(self):
    self.balance = self.deposit + self.balance
    return self.balance
  
  def your_account(self):
    self.quest = f"Hi {self.f_name }, What would you like ?"
    print(self.quest)
    self.user1_input = input("")
    if self.user1_input == "check balance":
      print("No problem I'll get that sorted for you")
      print(f"Your balance is {self.balance}")
      print(f"{self.f_name }, is there anything else you like help with ?")
      self.same_user = input("")
      if self.same_user == "yes":
        print(self.quest)
        self.user1_input = input("")
      else:
        print("Thank you good bye")
    elif self.user1_input == "deposit money":
      print("No problem I'll get that sorted for you")
      Services.money_in()
      print(f"{self.f_name }, is there anything else you like help with ?")
      self.same_user = input("")
      if self.same_user == "yes":
        self.quest
        self.user1_input = input("")
      else:
        print("Thank you good bye")
    elif self.user1_input == "take out money":
      print("No problem I'll get that sorted for you")
      Services.money_out()
      print(f"{self.f_name }, is there anything else you like help with ?")
      self.same_user = input("")
      if self.same_user == "yes":
        self.quest
        self.user1_input = input("")
      else:
        print("Thank you good bye")



# def serv_acc(self):
#   return self

# @Services(f_name="fd", withdraw=40 , deposit=50, func=serv_acc)
# def user1():
#   pass

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




