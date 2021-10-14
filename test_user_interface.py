import unittest
import user_interface

class TestUserInterface(unittest.TestCase):
    
    def test_validate_main_menu(self):
        """Validating if passing 1 tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(1)
        self.assertEqual(returned_value, (True, 1))

    def test_validate_main_menu_two(self):
        """Validating if passing 2 tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(2)
        self.assertEqual(returned_value, (True, 2))

    def test_validate_main_menu_three(self):
        """Validating if passing 3 tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(3)
        self.assertEqual(returned_value, (True, 3))

    def test_validate_main_menu_four(self):
        """Validating if passing 4 tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(4)
        self.assertEqual(returned_value, (True, 4))    

    def test_validate_main_menu_b(self):
        """Validating if passing a different number (False, None) will be returned"""
        returned_value = user_interface.validate_main_menu(5)
        self.assertEqual(returned_value, (False, None)) 




if __name__ == "__main__":
    unittest.main()