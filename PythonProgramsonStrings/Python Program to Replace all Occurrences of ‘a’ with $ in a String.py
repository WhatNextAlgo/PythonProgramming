s = input(r"Enter string: ")
new_str = ""
for x in s:
    if x.lower() == 'a':
        new_str = new_str + "$"
    else:
        new_str = new_str + x

print("Modified String: ",new_str)