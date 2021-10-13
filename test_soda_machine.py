import unittest
from cans import Cola, RootBeer
from customer import Customer
from coins import Quarter, Dime, Nickel, Penny
from soda_machine import SodaMachine

class TestSodaMachine(unittest.TestCase):
    def setUp(self):
        self.my_soda_machine = SodaMachine()

    def test_fill_register(self):
        """Test that its register list has a len of 88 """
        self.assertEqual(len(self.my_soda_machine.register), 88)
        print(len(self.my_soda_machine.register))

    def test_fill_inventory(self):    
        """test that its inventory list has a len of 30"""
        self.soda_machine_one = SodaMachine()
        self.assertEqual(len(self.soda_machine_one.inventory),30)

    def test_get_coin_from_register_one(self):  
        """ Test if Quarter can be returned from register """
        self.soda_machine_one = SodaMachine()
        returned_value = self.soda_machine_one.get_coin_from_register("Quarter")
        self.assertTrue(returned_value)

    def test_get_coin_from_register_two(self):  
        """ Test if Penny can be returned from register """
        self.soda_machine_one = SodaMachine()
        returned_value = self.soda_machine_one.get_coin_from_register("Penny")
        self.assertTrue(returned_value)

    def test_get_coin_from_register_three(self):  
        """ Test if Dime can be returned from register """
        self.soda_machine_one = SodaMachine()
        returned_value = self.soda_machine_one.get_coin_from_register("Dime")
        self.assertTrue(returned_value)

    def test_get_coin_from_register_Four(self):  
        """ Test if Nickle can be returned from register """
        self.soda_machine_one = SodaMachine()
        returned_value = self.soda_machine_one.get_coin_from_register("Nickel")
        self.assertTrue(returned_value)    

    def test_get_coin_from_register_Five(self):
        """ Test if invalid coin return a value from register """
        self.soda_machine_one = SodaMachine()
        returned_coin = self.soda_machine_one.get_coin_from_register("Peso")
        self.assertIsNone(returned_coin, None)

    def test_register_has_quarter(self):
        """Tests if register has quarters"""
        self.soda_machine_one = SodaMachine()
        returned_coin = self.soda_machine_one.register_has_coin('Quarter')
        self.assertTrue(returned_coin)

    def test_register_has_dime(self):
        """Tests if register has dimes"""
        self.soda_machine_one = SodaMachine()
        returned_coin = self.soda_machine_one.register_has_coin('Dime')
        self.assertTrue(returned_coin)

    def test_register_has_nickel(self):
        """Tests if register has nickels"""
        self.soda_machine_one = SodaMachine()
        returned_coin = self.soda_machine_one.register_has_coin('Nickel')
        self.assertTrue(returned_coin)

    def test_register_has_penny(self):
        """Tests if register has pennies"""
        self.soda_machine_one = SodaMachine()
        returned_coin = self.soda_machine_one.register_has_coin('Penny')
        self.assertTrue(returned_coin)

    def test_register_invalid_coin(self):
        """ Test if invalid coin returns false """
        self.soda_machine_one = SodaMachine()
        returned_coin = self.soda_machine_one.get_coin_from_register("Peso")
        self.assertFalse(returned_coin)

    def test_determine_change_value_a(self):
        self.soda_machine_one = SodaMachine()
        changed_value = self.soda_machine_one.determine_change_value(1.00, .50)
        self.assertGreater(changed_value, 0)
        print(changed_value)

    def test_determine_change_value_b(self):
        self.soda_machine_one = SodaMachine()
        changed_value = self.soda_machine_one.determine_change_value(1.00, 1.50)
        self.assertLess(changed_value, 0)
        print(changed_value)

    def test_determine_change_value_c(self):
        self.soda_machine_one = SodaMachine()
        changed_value = self.soda_machine_one.determine_change_value(1.00, 1.00)
        self.assertEqual(changed_value, 0)
        print(changed_value)

    def test_calculate_coin_value(self):
        self.soda_machine_one = SodaMachine()
        self.quarter = Quarter()
        self.dime = Dime()
        self.penny = Penny()
        self.nickle = Nickel()

        self.money_list = []
        self.money_list.append(self.quarter)
        self.money_list.append(self.dime)
        self.money_list.append(self.penny)
        self.money_list.append(self.nickle)

        self.assertEqual(self.soda_machine_one.calculate_coin_value(self.money_list), .41)

    def test_calculate_coin_value_with_zero(self):
        self.soda_machine_one = SodaMachine()
        self.money_list = []
        self.assertEqual(self.soda_machine_one.calculate_coin_value(self.money_list), 0)


if __name__ == "__main__":
    unittest.main()