#Multiply the List Elements
#A Python function that takes a list of values as input and returns the product of all the numbers in the list. 
#For example, given the input list [1, 3, 8], the function should return 24.

def mul_elements(lst):
    res = 1
    for item in lst:
        res *= item
    return res

mul_elements([1, 3, 8])