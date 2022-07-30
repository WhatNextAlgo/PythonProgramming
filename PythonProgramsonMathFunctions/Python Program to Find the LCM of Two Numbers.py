a = int(input("Enter first Number: "))
b = int(input("Enter Second Number: "))

if (a<b):
    min1= a
else:
    min1 = b

count = 1
while (1):
    if min1%a == 0 and min1%b == 0:
        count += 1
        print("LCM is: ",min1, "count : ",count)
        break
    count += 1
    min1 += 1


def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

lcm =  (a * b)/gcd(a,b)
print("LCM using GCD : ",lcm)