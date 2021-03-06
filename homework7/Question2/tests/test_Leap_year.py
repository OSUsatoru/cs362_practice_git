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
        self.argument4 = 400
        self.result4 = str(self.argument4) + " is a leap year\n"
        self.argument5 = 2000
        self.result5 = str(self.argument5) + " is a leap year\n"

    def test_FizzBuzz(self):
        with self.assertRaises(ValueError, msg = "Invalid input (type error)"):
            Leap_year_class(self.argument1).Leap_year()
        self.assertEqual(self.result2, Leap_year_class(self.argument2).Leap_year())

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1
        Leap_year_class(self.argument3).Leap_year()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.result3, capturedOutput1.getvalue())

        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        Leap_year_class(self.argument4).Leap_year()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.result4, capturedOutput2.getvalue())

        capturedOutput3 = io.StringIO()
        sys.stdout = capturedOutput3
        Leap_year_class(self.argument5).Leap_year()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.result5, capturedOutput3.getvalue())


if __name__ == "__main__":
    unittest.main()