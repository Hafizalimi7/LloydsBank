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
  def __init__(self, f_name, l_name, age, func, wage):
    super().__init__(f_name, l_name, age)
    self.func = func
    self.balance = 1000
    self.wage = wage
    self.monthly_wage = 0
    
  def __call__(self, *args):
    print(f"Hello {self.f_name} {self.l_name}, Welcome to Loyds Bank. How can i help you ?")
    print(f"{self.f_name } I would like to check my balance")
    print("No problem I'll get that sorted for you")
    print(f"Your balance is {self.balance}")
    return self.func(*args)
  
  def monthly(wage, m_w):
    any_user = BankAcc
    any_user.wage = wage
    any_user.monthly_wage = m_w

    any_user.monthly_wage += any_user.wage * 4
    return any_user.monthly_wage



def user1():
  tom = BankAcc
  tom.f_name = "Tom"
  wage = BankAcc.monthly
  print(f"tom earns {wage(50,0)} ")
user1()


# def monthly_pay(self):
#     return self

# def monthly_deposit():
#   print("can i put some money inside my account this month ?")
#   print("sure you can how much would you like like to put in ?")


# def Deposit():
#   monthly_wage += wage * 4
#   return monthly_wage

# def User2():
#   Danny = BankAcc("Danny", "Welbeck", 40, None, wage=1000)
#   depo = Deposit()
#   depo.Da
# @BankAcc(f_name="Mike", l_name="Jones", age=24, func=monthly_pay, wage=500)
# def deposit():
#   print("can i put some money inside my account ?")
#   print("sure you can how much would you like like to put in ?")
#   income = User1()
#   print(f"i'd like to put in {income}")
 
# deposit()

# user1 = BankAcc("d","d",34,None,500)
# print(user1.monthly_pay())
