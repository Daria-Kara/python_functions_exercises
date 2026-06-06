#Compute the Fibonacci Sequence
#The Fibonacci Sequence is computed based on the following formula:
#A Python function that computes the value of f(n) with a given n as input. 
#For example, given 7, the function should return 13.

def fib(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)

a = int(input("Enter a number: "))
print(fib(a))