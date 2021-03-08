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

        year=int(self.n)
        if year%4==0 and year%100!=0 or year%400==0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
