import unittest
import calculate_average

class test_case_average(unittest.TestCase):
    def setUp(self):
        self.a = [1,2,3,4,5]
        self.b = []
        self.c = [2,"str1","str2"]
    def test_cube(self):
        self.assertEqual(3, calculate_average.cal_ave(self.a))
        self.assertEqual("Empty list", calculate_average.cal_ave(self.b))
        self.assertEqual("Invalid input", calculate_average.cal_ave(self.c))

if __name__ == "__main__":
    unittest.main()