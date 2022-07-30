s = input("Enter String: ")
sub = input("Enter SubString: ")

if(s.find(sub) == -1):
      print("Substring not found in string!")
else:
      print("Substring in string!")