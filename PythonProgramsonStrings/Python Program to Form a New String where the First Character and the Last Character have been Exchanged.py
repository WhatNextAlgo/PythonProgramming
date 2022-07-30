s1 = input("Enter first string: ")


new_string = s1[-1:] + s1[1:-1] + s1[:1]
print(new_string)