import unittest
import calculator

class test_cal(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 2

    def test_addition(self):
        self.assertEqual(self.a+self.b, calculator.addition(self.a,self.b))

    def test_subtract(self):
        self.assertEqual(self.a-self.b, calculator.subtract(self.a,self.b))

    def test_multiply(self):
        self.assertEqual(self.a*self.b, calculator.multiply(self.a,self.b))

    def test_divider(self):
        self.assertEqual(self.a/self.b, calculator.divider(self.a,self.b))

if __name__ == "__main__":
    unittest.main()