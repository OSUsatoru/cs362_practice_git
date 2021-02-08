import unittest
import math
import calculate_cube

class test_case_cube(unittest.TestCase):
    def setUp(self):
        self.a = 5+math.sqrt(5)
        self.b = -5.5
        self.c = "str"
    def test_cube(self):
        self.assertEqual(math.pow(self.a,3), calculate_cube.cal_cube(self.a))
        self.assertEqual("Negative value", calculate_cube.cal_cube(self.b))
        self.assertEqual("Invalid input", calculate_cube.cal_cube(self.c))

if __name__ == "__main__":
    unittest.main()