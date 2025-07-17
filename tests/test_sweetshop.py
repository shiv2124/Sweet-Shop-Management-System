import unittest
from src.sweet import Sweet
from src.sweetshop import SweetShop

class TestSweetShop(unittest.TestCase):

    def setUp(self):
        self.shop = SweetShop()

    def test_add_sweet(self):
        sweet = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
        self.shop.add_sweet(sweet)
        self.assertEqual(len(self.shop.sweets), 1)
        self.assertEqual(self.shop.sweets[0].name, "Kaju Katli")

if __name__ == '__main__':
    unittest.main()