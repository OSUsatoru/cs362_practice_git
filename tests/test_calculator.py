import unittest
import calculator

class test_cal(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(5, calculator.addition(2,3))

    def test_subtract(self):
        self.assertEqual(-1, calculator.subtract(2,3))

    def test_multiply(self):
        self.assertEqual(6, calculator.multiply(2,3))

    def test_divider(self):
        self.assertEqual(2, calculator.divider(2,1))