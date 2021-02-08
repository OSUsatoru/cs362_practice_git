import unittest
import generate_name

class test_case_name(unittest.TestCase):
    def setUp(self):
        self.a = "Satoru"
        self.b = "Yamamoto"

        self.c = "only_first"
        self.d = ""

        self.e = ""
        self.f = "only_last"
    def test_cube(self):
        self.assertEqual("Satoru Yamamoto", generate_name.first_lastname(self.a, self.b))
        self.assertEqual("Empty first or last name", generate_name.first_lastname(self.c, self.d))
        self.assertEqual("Empty first or last name", generate_name.first_lastname(self.e, self.f))

if __name__ == "__main__":
    unittest.main()