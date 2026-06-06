#Check a Number is Prime
#A Python function that takes a number and checks the number is prime or not. 
#It should return True for being prime and False otherwise. Note that a prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself. 
#For example, the function should return True for the given number 7 and False for the given number 10.

def is_Prime(n):
  res = True
  for i in range(2, n):
    if n % i == 0:
    #Remainder is zero
      res = False
      break
  return res

num = int(input("Enter a number: "))

if is_Prime(num) == True:
  print("The number you entered is a prime number")
else:
  print("The number you entered is not a prime number")