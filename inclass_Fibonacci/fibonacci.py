
def fib(n):
  memo = [None]*(n+1)

  def fib_process(n):
    if n==0 or n==1:
      return 1
    if memo[n] != None:
      return memo[n]
    memo[n] = fib_process(n-1) + fib_process(n-2)
    return memo[n]

  return fib_process(n)
