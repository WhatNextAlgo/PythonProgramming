n = int(input("Enter Number  : "))

k= 0
for x  in range(2,n//2 + 1):
    if n % x == 0:
        k = k + 1

if k <= 0:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")
    