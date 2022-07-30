lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

for x  in range(lower,upper+1):
    if x %2 != 0 and  str(x) == str(x)[::-1]:
            print(x,end= " ")