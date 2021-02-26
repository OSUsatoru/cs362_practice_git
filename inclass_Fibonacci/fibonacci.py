class fibonacci_class:
    def __init__(self, n):
        self.n = n

    def fib(self):
        try:
            int(str(self.n))
        except ValueError:
            raise ValueError("Invalid input (type error)")
        if self.n < 0:
            return "Invalid input (sign error)"

        memo = [None]*(self.n+1)

        def fib_process(n):
            if n==0 or n==1:
                return 1
            if memo[n] != None:
                return memo[n]
            memo[n] = fib_process(n-1) + fib_process(n-2)
            return memo[n]

        return fib_process(self.n)

    def fac(self):
        try:
            int(str(self.n))
        except ValueError:
            raise ValueError("Invalid input (type error)")
        if self.n < 0:
            return "Invalid input (sign error)"

        def fact_process(n):
            if n == 0:
                return 1
            else:
                return n * fact_process(n-1)
        return fact_process(self.n)

