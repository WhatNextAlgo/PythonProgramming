s = input(r"Enter String: ")

for ind,x  in enumerate(s):
    if ind % 2 == 0:
        print(x,end = "")
