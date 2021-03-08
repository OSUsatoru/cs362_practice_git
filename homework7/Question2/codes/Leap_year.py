class Leap_year_class:
    def __init__(self, n):
        self.n = n
    def Leap_year(self):
        try:
            int(str(self.n))
        except ValueError:
            raise ValueError("Invalid input (type error)")
        if self.n < 0:
            return "Invalid input (sign error)"