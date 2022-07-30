n = input("Enter Number: ")

c = sum([int(x)**3 for x in n])

if int(n) == c:
    print(f"The {n} is an arsmtrong number.")
else:
    print(f"The {n} isn't a Armstong number")