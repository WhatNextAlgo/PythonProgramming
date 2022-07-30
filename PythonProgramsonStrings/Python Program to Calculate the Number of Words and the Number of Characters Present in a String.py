s = input("Enter String: ")

word_count = len(s.split(" "))
ch_count = len([x for x in s])

print("Number of words in the string:")
print(word_count)
print("Number of characters in the string:")
print(ch_count)


char=0
word=1
for i in s:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)