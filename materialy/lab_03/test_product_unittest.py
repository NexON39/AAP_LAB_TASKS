import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        # Stworz instancje Product przed kazdym testem
        self.product = Product("Laptop", 2999.99, 10)

    def test_add_stock_positive(self):
        # Wywolaj add_stock i sprawdz nowa wartosc quantity
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        # Uzyj self.assertRaises(ValueError)
        with self.assertRaises(ValueError):
            self.product.add_stock(-2)

    def test_remove_stock_positive(self):
        # Wywolaj remove_stock i sprawdz quantity
        self.product.remove_stock(3)
        self.assertEqual(self.product.quantity, 7)

    def test_remove_stock_too_much_raises(self):
        # Uzyj self.assertRaises(ValueError)
        with self.assertRaises(ValueError):
            self.product.remove_stock(15)

    def test_remove_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(-2)

    def test_is_available_when_in_stock(self):
        # Uzyj self.assertTrue
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        # Stworz produkt z quantity=0, uzyj self.assertFalse
        empty_product = Product("Myszka", 49.99, 0)
        self.assertFalse(empty_product.is_available())

    def test_total_value(self):
        # Uzyj self.assertEqual
        self.assertAlmostEqual(self.product.total_value(), 29999.90, places=2)

    def test_init_invalid_values(self):
        # Dodatkowo sprawdzam wartosci graniczne w __init__
        with self.assertRaises(ValueError):
            Product("Zepsuty", -10.0, 5)
        with self.assertRaises(ValueError):
            Product("Zepsuty", 10.0, -5)


if __name__ == "__main__":
    unittest.main()
