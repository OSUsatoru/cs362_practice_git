import unittest

import io
import sys
sys.path.append('..')

from codes.Leap_year import Leap_year_class

class Leap_year(unittest.TestCase):
    def setUp(self):
        self.argument1 = "string"
        self.result1 = "Invalid input (type error)"
        self.argument2 = -5
        self.result2 = "Invalid input (sign error)"
        self.argument3 = 80
        self.result3 = str(self.argument1) + "is a leap year"

    def test_FizzBuzz(self):
        with self.assertRaises(ValueError, msg = "Invalid input (type error)"):
            Leap_year_class(self.argument1).Leap_year()
        self.assertEqual(self.result2, Leap_year_class(self.argument2).Leap_year())



if __name__ == "__main__":
    unittest.main()