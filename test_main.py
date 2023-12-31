import unittest

from main import LloydsBank, BankAcc 


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
    first_name = self.user1.first_name()
    self.assertEqual(first_name, "Tom")

  def test_last_name_meth(self):
    last_name = self.user1.last_name()
    self.assertEqual(last_name, "Bradly")
  
  def test_user_age(self):
    age = self.user1.p_age()
    self.assertEqual(age, self.user1.age)
  
# class TestBankCls(TestLloydsCls, unittest.TestCase):
#   class Bank:
#     customer1 = BankAcc("John", "Smith", 34, None, 2000)

#     def test_end_of_month_meth(self):
#       month_wage = self.customer1.end_of_month_salary()
#       self.assertEqual(month_wage, 45)


if __name__ == "__main__":
  unittest.main()
