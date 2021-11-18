import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    # Create a pub object
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

        # Create Drink Objects
        self.drink_1 = Drink("Pumpkin Juice", 7.00)
        self.drink_2 = Drink("Butterbeer", 6.00)
        self.drink_3 = Drink("Chocolate Frogs", 12.00)
        self.drink_4 = Drink("Firewhisky", 4.00)

        # Create Customer objects
        self.customer_1 = Customer("Hermione", 17.00)
        self.customer_2 = Customer("Harry Potter", 14.00)



    def test_pub_has_a_name(self):
        expected = "The Prancing Pony"
        actual = self.pub.name
        self.assertEqual(expected, actual)

    def test_pub_has_a_till(self):
        expected = 100.00
        actual = self.pub.till
        self.assertEqual(expected, actual)

    def test_pub_can_add_drinks(self):
        self.pub.add_drink(self.drink_2)
        expected = 1
        actual = self.pub.count_drinks()
        self.assertEqual(expected, actual)

    def test_pub_can_serve_drink(self):
        # Add 3 drinks in a list, sell 1
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_3)
        self.pub.add_drink(self.drink_4)
        # Serve to customer
        self.pub.serve_drink(self.customer_1, self.drink_3)
        # Check how many drinks left in a pub
        self.assertEqual(2, self.pub.count_drinks())
        # Check customer's wallet
        self.assertEqual(5.00, self.customer_1.wallet)
        # Check pub's till
        self.assertEqual(112.00, self.pub.till)
