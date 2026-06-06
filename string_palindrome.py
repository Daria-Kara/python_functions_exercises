#Check if a String is Palindrome
#A Python function that takes a string and returns True if it is palindrome. A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward. 
#For example, given the string "abc" the function should return False. 
#But, given the string "aba", the function should return True.

def pali(s):
  for i in range (int(len(s) / 2)):
    if s[i] != s[-1-i]:
      return False

  return True

s = input("Enter a word: ")
print(pali(s))