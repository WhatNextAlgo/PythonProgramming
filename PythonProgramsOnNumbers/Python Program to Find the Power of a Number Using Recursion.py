def power_of_number(base, exp):
    if exp == 1:
        return base
    
    return base * power_of_number(base,exp -1)


base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power_of_number(base,exp))