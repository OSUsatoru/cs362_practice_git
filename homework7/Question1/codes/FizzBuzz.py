class FizzBuzz_class:
    def FizzBuzz(self):
        for i in range(1,101):
            if i%3==0:
                print("Fizz", end="")
            else:
                print(i,end="")
            if i!=100:
                print(" ",end="")