import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):

    def setUp(self):
        # Create Drink object
        self.drink_1 = Drink("Pumpkin Juice", 7.00)
