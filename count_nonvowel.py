#Count Non-Vowel Characters
#A Python function that takes a string and returns the number of non-vowel characters in that string. 
#Vowel characters in English are "a", "e", "i", "o", and "u". 
#For example, given the string "abcdA", the function should return 3.

def count_non_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char not in vowels:
            count += 1

    return count

a = (input("Enter a string: "))
count_non_vowels(a)
