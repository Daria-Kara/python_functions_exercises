#Sort Hyphened-Seperated Words
#A Python function that takes a sequence of words that are separated by hyphens as input and returns the words in a hyphen-separated sequence after sorting the words alphabetically. 
#For example, given the string "green-red-yellow-black-white", the function should return "black-green-red-white-yellow".

unsorted_string = sorted("green-red-yellow-black-white".split("-"))
print("-".join(unsorted_string))