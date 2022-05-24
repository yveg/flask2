import unittest

from employee import Employee

class EmployeeTest(unittest.TestCase):
    """"
    Python runs the setUp() method before running
    each method starting with test_. Any objects created in the setUp() method
    are then available in each test method you write."""

    def setUp(self) -> None:
        self.our_employee = Employee("Recep","XXXX",10000)
    
    def test_give_default(self):
        self.raised_salary = self.our_employee.give_raise()
        self.assertEqual(self.raised_salary,15000)
        
    def test_give_custom_raise(self):
        self.raised_more_salary = self.our_employee.give_raise(6000)
        self.assertEqual(self.raised_more_salary,16000)



if __name__ == "__main__":
    unittest.main()