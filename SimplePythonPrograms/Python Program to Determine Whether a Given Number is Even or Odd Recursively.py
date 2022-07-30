
def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2)) # untill 0/1

n  =  int(input("Enter Number : "))

if check(n) == True:
    print(f"{n} is even number")
else:
    print(f"{n} is odd number")





