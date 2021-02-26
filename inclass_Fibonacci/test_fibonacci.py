import unittest
import fibonacci

class fib(unittest.TestCase):
    def setUp(self):
        self.test1_result = 2
        self.test1_argument = 3
        self.test2_result = 55
        self.test2_argument = 10
        self.test3_result = 89
        self.test3_argument = 11

    def test_fibo(self):
        self.assertEqual(self.test1_result, fibonacci.fib(self.test1_argument))
        self.assertEqual(self.test2_result, fibonacci.fib(self.test2_argument))
        self.assertEqual(self.test3_result, fibonacci.fib(self.test3_argument))

if __name__ == "__main__":
    unittest.main()