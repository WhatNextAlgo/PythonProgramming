n=int(input("Enter a number: "))
sum1  =0 
for x in range(1,n + 1):
    sum1 = sum1 + x
    print(x, sep= " ", end=" ")
    if (x < n):
        print("+",sep=" ",end=" ") 

print(" = ",sum1)

