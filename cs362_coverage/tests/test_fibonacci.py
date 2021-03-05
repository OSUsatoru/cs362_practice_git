import unittest
import sys
sys.path.append('..')

from fibonacci import fibonacci_class

class fib(unittest.TestCase):
    def setUp(self):
        self.test1_result = 89
        self.test1_argument = 10
        self.test2_result = "Invalid input (sign error)"
        self.test2_argument = -5
        self.test3_result = "Invalid input (type error)"
        self.test3_argument = 1.2
        self.test4_result = "Invalid input (type error)"
        self.test4_argument = "input string"

        self.test5_result = 3628800
        self.test5_argument = 10
        self.test6_result = "Invalid input (sign error)"
        self.test6_argument = -5
        self.test7_result = "Invalid input (type error)"
        self.test7_argument = 1.2
        self.test8_result = "Invalid input (type error)"
        self.test8_argument = "input string"

    def test_fibo(self):
        self.assertEqual(self.test1_result, fibonacci_class(self.test1_argument).fib())
        self.assertEqual(self.test2_result, fibonacci_class(self.test2_argument).fib())
        with self.assertRaises(ValueError, msg = "Invalid input (type error)"):
            fibonacci_class(self.test3_argument).fib()
        with self.assertRaises(ValueError, msg = "Invalid input (type error)"):
            fibonacci_class(self.test4_argument).fib()

    def test_fact(self):
        self.assertEqual(self.test5_result, fibonacci_class(self.test5_argument).fac())
        self.assertEqual(self.test6_result, fibonacci_class(self.test6_argument).fac())
        with self.assertRaises(ValueError, msg = "Invalid input (type error)"):
            fibonacci_class(self.test7_argument).fac()
        with self.assertRaises(ValueError, msg = "Invalid input (type error)"):
            fibonacci_class(self.test8_argument).fac()

if __name__ == "__main__":
    unittest.main()