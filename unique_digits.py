#Count the Unique Digits in an Integer
#A Python function that takes a positive integer and returns the number of unique digits in that integer. 
#For example, given the integer 12315, the function should return 4.

def unique_digits(n):
    st = str(n)             # convert from integer to string
    s = set([])             # create an empty set

    # for each digit (character) in the st
    for digit in st:
        s.add(digit)        # add the digit to the set
    return len(s)

c = int(input("Enter an integer: "))
unique_digits(c)