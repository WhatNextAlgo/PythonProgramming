l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))

lst = [(x,x*x) for x in range(l_range,u_range + 1)]
print(lst)
