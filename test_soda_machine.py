import unittest
from cans import Can, Cola, OrangeSoda, RootBeer
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
        self.assertEqual(len(self.my_soda_machine.inventory), 30)

    def test_get_coin_from_register_one(self):  
        """ Test if Quarter can be returned from register """
        returned_value = self.my_soda_machine.get_coin_from_register("Quarter")
        self.assertTrue(returned_value)

    def test_get_coin_from_register_two(self):  
        """ Test if Penny can be returned from register """
        returned_value = self.my_soda_machine.get_coin_from_register("Penny")
        self.assertTrue(returned_value)

    def test_get_coin_from_register_three(self):  
        """ Test if Dime can be returned from register """
        returned_value = self.my_soda_machine.get_coin_from_register("Dime")
        self.assertTrue(returned_value)

    def test_get_coin_from_register_Four(self):  
        """ Test if Nickle can be returned from register """
        returned_value = self.my_soda_machine.get_coin_from_register("Nickel")
        self.assertTrue(returned_value)    

    def test_get_coin_from_register_Five(self):
        """ Test if invalid coin return a value from register """
        returned_coin = self.my_soda_machine.get_coin_from_register("Peso")
        self.assertIsNone(returned_coin, None)

    def test_register_has_quarter(self):
        """Tests if register has quarters"""
        self.quarter = Quarter()
        returned_coin = self.my_soda_machine.register_has_coin(self.quarter.name)
        self.assertTrue(returned_coin)

    def test_register_has_dime(self):
        """Tests if register has dimes"""
        self.dime = Dime()
        returned_coin = self.my_soda_machine.register_has_coin(self.dime.name)
        self.assertTrue(returned_coin)

    def test_register_has_nickel(self):
        """Tests if register has nickels"""
        self.nickel = Nickel()
        returned_coin = self.my_soda_machine.register_has_coin(self.nickel.name)
        self.assertTrue(returned_coin)

    def test_register_has_penny(self):
        """Tests if register has pennies"""
        self.penny = Penny()
        returned_coin = self.my_soda_machine.register_has_coin(self.penny.name)
        self.assertTrue(returned_coin)

    def test_register_invalid_coin(self):
        """ Test if invalid coin returns false """
        returned_coin = self.my_soda_machine.get_coin_from_register("Peso")
        self.assertFalse(returned_coin)

    def test_determine_change_value_a(self):
        """Determine Change return with Total_price higher """
        changed_value = self.my_soda_machine.determine_change_value(1.00, .50)
        self.assertGreater(changed_value, 0)
        print(changed_value)

    def test_determine_change_value_b(self):
        """Determine Change return with soda_price higher """
        changed_value = self.my_soda_machine.determine_change_value(1.00, 1.50)
        self.assertLess(changed_value, 0)
        print(changed_value)

    def test_determine_change_value_c(self):
        """Determine Change return with two equal values from register """
        changed_value = self.my_soda_machine.determine_change_value(1.00, 1.00)
        self.assertEqual(changed_value, 0)
        print(changed_value)

    def test_calculate_coin_value(self):
        """Test to pass list coins and make sure the list update its value"""
        self.quarter = Quarter()
        self.dime = Dime()
        self.penny = Penny()
        self.nickle = Nickel()

        self.money_list = []
        self.money_list.append(self.quarter)
        self.money_list.append(self.dime)
        self.money_list.append(self.penny)
        self.money_list.append(self.nickle)

        self.assertEqual(self.my_soda_machine.calculate_coin_value(self.money_list), .41)

    def test_calculate_coin_value_with_zero(self):
        """Test if List change value after passing empty list"""
        self.money_list = []
        self.assertEqual(self.my_soda_machine.calculate_coin_value(self.money_list), 0)

    def test_get_inventory_soda_a(self):
        """Test to make sure the soda name entered is returned correctly"""
        self.cola = Cola()
        self.orange_soda = OrangeSoda()
        self.root_beer = RootBeer()
        self.soda_inventory_one = self.my_soda_machine.get_inventory_soda(self.cola.name)
        self.soda_inventory_two = self.my_soda_machine.get_inventory_soda(self.orange_soda.name)
        self.soda_inventory_three = self.my_soda_machine.get_inventory_soda(self.root_beer.name)
        self.assertEqual(self.soda_inventory_one.name, "Cola")
        self.assertEqual(self.soda_inventory_two.name, "Orange Soda")
        self.assertEqual(self.soda_inventory_three.name, "Root Beer")
        
    def test_get_inventory_soda_b(self):
        """Test if it return a Soda if given incorrect unput - None is returned"""
        self.soda_inventory_one = self.my_soda_machine.get_inventory_soda('Mountain Dew')
        self.assertIsNone(self.soda_inventory_one)

    def test_return_inventory(self):
        """ Test if the length of inventory is correct after adding a can"""
        my_can = Cola()
        self.my_soda_machine.return_inventory(my_can)  
        self.assertEqual(len(self.my_soda_machine.inventory), 31)  

    def test_deposit_coins_into_register(self):
        """ Test Deposit coint into register and confirm new length"""
        self.quarter = Quarter()
        self.dime = Dime()
        self.penny = Penny()
        self.nickle = Nickel()

        self.money_list = []
        self.money_list.append(self.quarter)
        self.money_list.append(self.dime)
        self.money_list.append(self.penny)
        self.money_list.append(self.nickle)

        self.my_soda_machine.deposit_coins_into_register(self.money_list)
        self.assertEqual(len(self.my_soda_machine.register), 92)


if __name__ == "__main__":
    unittest.main()