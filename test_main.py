import unittest
from unittest.mock import patch

from main import LloydsBank, BankAcc , PasswordCheck, Services


class TestLloydsCls(unittest.TestCase):
  user1 = LloydsBank("Tom", "Bradly", 11) 

  """creating another object""" 
  class Customer:
    # user1 = LloydsBank("Tom", "Bradly", 11) 
    def __init__(self,f_name, l_name, age) -> None:
      pass
  user2 = Customer("Mike", "Jones", 30)

  """testing if object exists"""
  def test_obj_in_class(self):
   self.assertIsInstance(self.user1, LloydsBank)
   self.assertNotIsInstance(self.user2, LloydsBank)

   """testing LloydsBank methods"""

  def test_first_name_meth(self):
    # first_name = self.user1.first_name()
    self.assertEqual(self.user1.first_name(), "Tom")

  def test_last_name_meth(self):
    # last_name = self.user1.last_name()
    self.assertEqual(self.user1.last_name(), "Bradly")
  
  def test_user_age(self):
    # age = self.user1.p_age()
    self.assertEqual(self.user1.p_age(), self.user1.age)
  
class TestBankCls(TestLloydsCls, unittest.TestCase):
 
    customer1 = BankAcc("John", "Smith", 34, None, 2000)

    def test_end_of_month_meth(self):
      month_wage = self.customer1.end_of_month_salary()
      self.assertEqual(month_wage, 8000)
    
    def test_year_salary_meth(self):
      year_wage = self.customer1.yearly_salary()
      self.assertEqual(year_wage, 96000)

class TestPasswordCheck(TestBankCls, unittest.TestCase):
  user3 = PasswordCheck
  passwords = user3.password=1234
  securityq = user3.secrurity_keyword="Letter"
  
  user5 = PasswordCheck
  first_name = user5.f_name="Max"
  last_name = user5.l_name="Jon"
  str = f"Hello {first_name} {last_name}, Welcome to Loyds Bank. Can you type in your password?"
  
  
  @patch('main.PasswordCheck.checking_correct_password', return_value=passwords)
  def test_password_correct(self, input):
      self.assertEqual(self.user3.checking_correct_password(), 1234)
      
  @patch('main.PasswordCheck.checking_correct_password', return_value=passwords)
  def test_passwd_not_correct(self, input):
    self.assertNotEqual(self.user3.checking_correct_password(), "hello")
  
  @patch('main.PasswordCheck.checking_correct_password', return_value=securityq)
  def test_securityq__correct(self, input):
    self.assertEqual(self.user3.checking_correct_password(), "Letter")
        
  @patch('main.PasswordCheck.checking_correct_password', return_value=securityq)
  def test_securityq_not_correct(self, input):
     self.assertNotEqual(self.user3.checking_correct_password(), "Numbers")
  
  @patch('main.PasswordCheck.__call__', return_value=str)
  def test_call_method(self, input):
    self.assertEqual(self.user5.__call__(),"Hello Max Jon, Welcome to Loyds Bank. Can you type in your password?")
  
class TestServicesCls(TestPasswordCheck, unittest.TestCase):
  def serv_acc(self):
   return self
  
  @Services(f_name="fd", withdraw=40 , deposit=50, func=serv_acc)
  def user1():
    pass

  
  new_user = Services("Fred", withdraw=40 , deposit=50, func=serv_acc)
 
  
  @patch('builtins.input')
  def test_query_y(self, input):
    
    # print(self.new_user.__call__(self))
    self.assertEqual(self.new_user.__call__(), "check balance")
  

    
    


if __name__ == "__main__":
  unittest.main()
