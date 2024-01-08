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
    # print(f"Hello {self.f_name} {self.l_name}, Welcome to Loyds Bank. Can you type in your password?")
    # print(self.checking_correct_password()
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
  def __init__(self, f_name ,withdraw, deposit):
    self.f_name = f_name
    self.withdraw = withdraw
    self.deposit = deposit
    # self.func = func

  # def __call__(self):
    # print(self)
    # return self.your_account()
    # return self.func()
  
  def money_out(self):
    self.balance - self.withdraw
    return self.balance
  
  def money_in(self):
    self.balance + self.deposit
    return self.balance
  
  def your_account(self):
    self.quest = f"Hi {self.f_name }, What would you like ?"
    self.user1_input = input("")
    if self.user1_input == "check balance":
      return f"No problem I'll get that sorted for you\nYour balance is {self.balance} Mr {self.f_name}"
    elif self.user1_input == "deposit money":
      return f"We have put in £{self.deposit}\nYour balance is now {self.money_in()} Mr {self.f_name}"
    elif self.user1_input == "take out money":
      return f"We have withdrawn £{self.withdraw} from your account\nYour balance is now {self.money_out()} Mr {self.f_name}"



# @Services(f_name="fd", withdraw=40 , deposit=50, func=None)
# def serv_acc(self):
#   return self

# @Services(f_name="fd", withdraw=40 , deposit=50, func=serv_acc)
# def user1():
#   pass

# ab = Services("max", 30, 100, None)
# print(f"{ab.balance} and {ab.money_in()}")
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




