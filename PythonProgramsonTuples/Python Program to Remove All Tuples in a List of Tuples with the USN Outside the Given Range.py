y=[('a','12CS039'),('b','12CS320'),('c','12CS055'),('d','12CS100')]
low=int(input("Enter lower roll number (starting with 12CS):"))
up=int(input("Enter upper roll number (starting with 12CS):"))
l = '12CS0' + str(low)
u = '12CS' + str(up)

for x in y:
    if x[1] > l and x[1] < u:
        print(x)
