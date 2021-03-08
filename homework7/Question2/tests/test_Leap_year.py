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
        self.result3 = str(self.argument3) + " is a leap year\n"

    def test_FizzBuzz(self):
        with self.assertRaises(ValueError, msg = "Invalid input (type error)"):
            Leap_year_class(self.argument1).Leap_year()
        self.assertEqual(self.result2, Leap_year_class(self.argument2).Leap_year())

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        Leap_year_class(self.argument3).Leap_year()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.result3, capturedOutput.getvalue())


if __name__ == "__main__":
    unittest.main()