#Pangram means a sentence containing every letter of the alphabet.

from string import ascii_lowercase as asc_lower

def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
s = input(r"Enter string: ")

if check(s):
    print("The string is a pangram")
else:
    print("The string isn't a pangram")
