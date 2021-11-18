import unittest
from src.customer import Customer
from src.drink import Drink


class TestCustomer(unittest.TestCase):

    def setUp(self):
        # Create a Customer object
        self.customer = Customer("Ronald Weasley", 20.00)

    def test_customer_has_name(self):
        self.assertEqual("Ronald Weasley", self.customer.name)