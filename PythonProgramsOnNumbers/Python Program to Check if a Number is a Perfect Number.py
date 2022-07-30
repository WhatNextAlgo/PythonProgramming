n = int(input("Enter Number : "))

sum  = 0

for x in range(1,n):
    if n % x == 0:
        sum  = sum + x


if sum == n:
    print(f"{n} is a prefect number")
else:
    print(f"{n} is not a prefect number")
