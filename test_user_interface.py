import unittest
import user_interface
from cans import Cola, OrangeSoda, RootBeer
from coins import Quarter, Dime, Nickel, Penny

class TestValidateMainMenu(unittest.TestCase):
    
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


class TestTryParseInt(unittest.TestCase):

    def test_try_parse_int(self):
        """Testing '10', needs to return int value 10"""
        returned_value = user_interface.try_parse_int('10')
        self.assertEqual(returned_value, 10)
        pass

    def test_try_parse_int_b(self):
        """Tests 'hello', needs to return 0"""
        returned_value = user_interface.try_parse_int('hello')
        self.assertEqual(returned_value, 0)


class TestGetUniqueCanNames(unittest.TestCase):

    def test_get_unique_can_names(self):
        """Tests list returns only 3 names in list."""
        self.cola = Cola()
        self.cola_one = Cola()
        self.orange_soda = OrangeSoda()
        self.orange_soda_one = OrangeSoda()
        self.root_beer = RootBeer()
        self.root_beer_one = RootBeer()
        
        self.my_soda = []

        self.my_soda.append(self.cola)
        self.my_soda.append(self.cola_one)
        self.my_soda.append(self.orange_soda)
        self.my_soda.append(self.orange_soda_one)
        self.my_soda.append(self.root_beer)
        self.my_soda.append(self.root_beer_one)

        returned_value = user_interface.get_unique_can_names(self.my_soda)
        self.assertEqual(len(returned_value), 3)

    def test_get_unique_can_names_b(self):
        """Tests if empty list is returned"""
        self.my_soda = []

        returned_value = user_interface.get_unique_can_names(self.my_soda)
        self.assertEqual(len(returned_value), 0)

       
class TestDisplayPaymentValue(unittest.TestCase):

    def test_display_payment_value(self):
        """Tests if returned value is .41"""
        self.quarter = Quarter()
        self.dime = Dime()
        self.nickel = Nickel()
        self.penny = Penny()

        self.wallet = []

        self.wallet.append(self.quarter)
        self.wallet.append(self.dime)
        self.wallet.append(self.nickel)
        self.wallet.append(self.penny)

        returned_value = user_interface.display_payment_value(self.wallet)
        self.assertEqual(returned_value, .41)

    def test_display_payment_value_b(self):
        """Tests returned value 0"""
        self.wallet = []

        returned_value = user_interface.display_payment_value(self.wallet)
        self.assertEqual(returned_value, 0)

    
class TestValidateCoinSelection(unittest.TestCase):
        
    def test_validate_coin_selection_a(self):
        """validate that input 1 will return the right tuple"""
        returned_value = user_interface.validate_coin_selection(1)
        self.assertEqual(returned_value, (True, "Quarter"))

    def test_validate_coin_selection_b(self):
        """validate that input 2 will return the right tuple"""
        returned_value = user_interface.validate_coin_selection(2)
        self.assertEqual(returned_value, (True, "Dime"))

    def test_validate_coin_selection_c(self):
        """validate that input 3 will return the right tuple"""
        returned_value = user_interface.validate_coin_selection(3)
        self.assertEqual(returned_value, (True, "Nickel"))

    def test_validate_coin_selection_d(self):
        """validate that input 4 will return the right tuple"""
        returned_value = user_interface.validate_coin_selection(4)
        self.assertEqual(returned_value, (True, "Penny"))

    def test_validate_coin_selection_e(self):
        """validate that input 5 will return the right tuple"""
        returned_value = user_interface.validate_coin_selection(5)
        self.assertEqual(returned_value, (True, "Done"))
    
    def test_validate_coin_selection_f(self):
        """validate that different input  will return False, None tuple"""
        returned_value = user_interface.validate_coin_selection(6)
        self.assertEqual(returned_value, (False, None))       

if __name__ == "__main__":
    unittest.main()