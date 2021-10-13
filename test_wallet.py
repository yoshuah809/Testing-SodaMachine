import unittest
from coins import Quarter, Dime, Nickel, Penny
from wallet import Wallet

class TestWallet(unittest.TestCase):
    def setUp(self):
        self.my_wallet = Wallet()

    def test_fill_wallet(self):
        self.assertEqual(len(self.my_wallet.money), 88)
        print(len(self.my_wallet.money))


if __name__ == "__main__":
    unittest.main()