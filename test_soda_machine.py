import unittest
from cans import Cola
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

if __name__ == "__main__":
    unittest.main()