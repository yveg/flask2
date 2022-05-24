import unittest
from name_function import get_formatted_name
"""Common Funciton That we can use 
assertEqual(a, b) Verify that a == b
assertNotEqual(a, b) Verify that a != b
assertTrue(x) Verify that x is True
assertFalse(x) Verify that x is False
assertIn(item, list) Verify that item is in list
assertNotIn(item, list) Verify that item is not in list
"""

class NameTestCase(unittest.TestCase):
    """Test for 'name_funciton.py'."""
    def test_first_last_name(self):
        """Do name like 'janis Joplin' work?"""
        formatted_name = get_formatted_name('Janis','Joplin')
        self.assertEqual(formatted_name,'Janis Joplin')#verify that a result you received matches the result you expected to receive.

    def test_first_last_middle_name(self):
        """Do name like 'wolfganga Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()