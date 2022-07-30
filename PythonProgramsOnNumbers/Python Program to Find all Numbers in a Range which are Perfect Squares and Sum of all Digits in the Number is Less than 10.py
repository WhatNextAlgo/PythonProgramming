lower =int(input("Enter lower range: "))
upper =int(input("Enter upper range: "))


lst = [x for x in range(lower,upper + 1) if (int(x ** 0.5))**2 == x and sum([int(x) for x in str(x)]) < 10]
print(lst)