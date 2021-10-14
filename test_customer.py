import unittest
from cans import Cola
from customer import Customer
from coins import Quarter, Dime, Nickel, Penny

class TestGetWalletCoin(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()


    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.value, .25)

    def test_can_return_dime(self):
        """Pass in 'Dime', method should return a Dime instance"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.value, .10)

    def test_can_return_nickel(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.value, .05)

    def test_can_return_penny(self):
        """Pass in 'Penny', method should return a Penny instance"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.value, .01)

    def test_no_string(self):
        """Passing in an empty string returns not valid."""
        returned_coin = self.customer.get_wallet_coin(' ')
        self.assertIsNone(returned_coin, None)



class TestAddCoinsToWallet(unittest.TestCase):
    """Tests for Customer's add_coinst_to_wallet method"""

    def setUp(self):
      self.customer = Customer()

    def test_add_coinst_to_wallet(self):  
        """"Pass in a list of 3 coins, test that the len of the customer’s wallet’s money list went up by
            3"""
        array_size =  len(self.customer.wallet.money)  
        self.customer.add_coins_to_wallet([Penny(), Penny(), Penny()])
        self.assertEqual(len(self.customer.wallet.money), array_size + 3)

    def test_empty_wallet_add_coinst_to_wallet(self):  
        """"Pass Empty walle, test that the len of the customer’s wallet’s money stays the same"""
        array_size =  len(self.customer.wallet.money)  
        self.customer.add_coins_to_wallet([])
        self.assertEqual(len(self.customer.wallet.money), array_size)    
        

class TestAddCanToBackpack(unittest.TestCase):
    """Tests if Cola object is passed and testing the length of the customers backpack's purchased_cans list went up by 1"""

    def setUp(self):
        self.customer = Customer()

    def test_backpack_one(self):
        backpack = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(Cola())
        self.assertEqual(len(self.customer.backpack.purchased_cans), backpack + 1)
        print(len(self.customer.backpack.purchased_cans))


    def test_backpack_two(self):
        backpack = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(Cola())
        self.assertEqual(len(self.customer.backpack.purchased_cans), backpack + 1)
        print(len(self.customer.backpack.purchased_cans))

    def test_backpack_three(self):
        backpack = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(Cola())
        self.assertEqual(len(self.customer.backpack.purchased_cans), backpack + 1)
        print(len(self.customer.backpack.purchased_cans))


if __name__ == "__main__":
    unittest.main()
