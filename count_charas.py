#Count the Characters
#A Python function that takes a string as input and returns a dictionary that stores the frequency of each character in the input string. 
#For example, given the string "abca", the function should return {'a': 2, 'b': 1, 'c': 1}.

def count_characters(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

result = count_characters("abca")
print(result)