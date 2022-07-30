n=int(input("Enter a number: "))

for x in range(0,n):
    for y in range(0,n):
        if (x == y):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()