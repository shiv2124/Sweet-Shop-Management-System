import unittest
from src.sweetshop import SweetShop
from src.sweet import Sweet

class TestSweetShop(unittest.TestCase):

    def setUp(self):
        self.shop = SweetShop()

    def test_add_sweet(self):
        sweet = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
        self.shop.add_sweet(sweet)
        self.assertEqual(len(self.shop.sweets), 1)
        self.assertEqual(self.shop.sweets[0].name, "Kaju Katli")

    def test_delete_sweet(self):
        sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
        sweet2 = Sweet(id=1002, name="Gulab Jamun", category="Milk-Based", price=10, quantity=50)
        self.shop.add_sweet(sweet1)
        self.shop.add_sweet(sweet2)

        self.shop.delete_sweet(1001)
        
        self.assertEqual(len(self.shop.sweets), 1)
        self.assertEqual(self.shop.sweets[0].id, 1002)
    
    def test_view_sweets(self):
        sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
        sweet2 = Sweet(id=1002, name="Gulab Jamun", category="Milk-Based", price=10, quantity=50)
        
        self.shop.add_sweet(sweet1)
        self.shop.add_sweet(sweet2)

        sweets = self.shop.view_sweets()
        self.assertEqual(len(sweets), 2)
        self.assertEqual(sweets[0].name, "Kaju Katli")
        self.assertEqual(sweets[1].name, "Gulab Jamun")
    
    def test_search_by_name(self):
        sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
        sweet2 = Sweet(id=1002, name="Gulab Jamun", category="Milk-Based", price=10, quantity=50)
        sweet3 = Sweet(id=1003, name="Gajar Halwa", category="Vegetable-Based", price=30, quantity=15)

        self.shop.add_sweet(sweet1)
        self.shop.add_sweet(sweet2)
        self.shop.add_sweet(sweet3)

        result = self.shop.search_by_name("Gulab Jamun")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1002)
    
    def test_search_by_category(self):
        sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
        sweet2 = Sweet(id=1002, name="Gulab Jamun", category="Milk-Based", price=10, quantity=50)
        sweet3 = Sweet(id=1003, name="Badam Barfi", category="Nut-Based", price=60, quantity=25)

        self.shop.add_sweet(sweet1)
        self.shop.add_sweet(sweet2)
        self.shop.add_sweet(sweet3)

        result = self.shop.search_by_category("Nut-Based")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(sweet.category == "Nut-Based" for sweet in result))
    
    def test_search_by_price_range(self):
        sweet1 = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=20)
        sweet2 = Sweet(id=1002, name="Gulab Jamun", category="Milk-Based", price=10, quantity=50)
        sweet3 = Sweet(id=1003, name="Rasgulla", category="Milk-Based", price=40, quantity=30)

        self.shop.add_sweet(sweet1)
        self.shop.add_sweet(sweet2)
        self.shop.add_sweet(sweet3)

        result = self.shop.search_by_price_range(20, 50)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(20 <= sweet.price <= 50 for sweet in result))
    
    def test_purchase_sweet_success(self):
        sweet = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50, quantity=10)
        self.shop.add_sweet(sweet)

        self.shop.purchase_sweet(1001, 3)
        self.assertEqual(self.shop.sweets[0].quantity, 7)

    def test_purchase_insufficient_stock(self):
        sweet = Sweet(id=1002, name="Gulab Jamun", category="Milk-Based", price=10, quantity=5)
        self.shop.add_sweet(sweet)

        with self.assertRaises(ValueError):
            self.shop.purchase_sweet(1002, 10)
    
    def test_restock_sweet(self):
        sweet = Sweet(id=1003, name="Rasgulla", category="Milk-Based", price=40, quantity=10)
        self.shop.add_sweet(sweet)

        self.shop.restock_sweet(1003, 15)
        self.assertEqual(self.shop.sweets[0].quantity, 25)

if __name__ == '__main__':
    unittest.main()