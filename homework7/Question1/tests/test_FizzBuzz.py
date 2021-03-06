import unittest

import io
import sys
sys.path.append('..')

from codes.FizzBuzz import FizzBuzz_class

class FizzBuzz(unittest.TestCase):
    def setUp(self):
        self.test1 = "1 2 Fizz 4 5 Fizz 7 8 Fizz 10 11 Fizz 13 14 Fizz 16 17 Fizz 19 20 Fizz 22 23 Fizz 25 26 Fizz 28 29 Fizz 31 32 Fizz 34 35 Fizz 37 38 Fizz 40 41 Fizz 43 44 Fizz 46 47 Fizz 49 50 Fizz 52 53 Fizz 55 56 Fizz 58 59 Fizz 61 62 Fizz 64 65 Fizz 67 68 Fizz 70 71 Fizz 73 74 Fizz 76 77 Fizz 79 80 Fizz 82 83 Fizz 85 86 Fizz 88 89 Fizz 91 92 Fizz 94 95 Fizz 97 98 Fizz 100"
        self.test2 = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 Fizz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Fizz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 Fizz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 Fizz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 Fizz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz"
        self.test3 = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz"
    def test_FizzBuzz(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        FizzBuzz_class().FizzBuzz()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.test3, capturedOutput.getvalue())

if __name__ == "__main__":
    unittest.main()