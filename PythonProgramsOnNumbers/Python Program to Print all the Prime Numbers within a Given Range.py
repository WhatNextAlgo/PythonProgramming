upper = int(input("Enter upper limit : "))

for x in range(2, upper + 1):
    k = 0

    for y in range(2, x//2 + 1):
        if (x%y == 0):
            k = k +1 

    if (k <= 0):
        print(x)


