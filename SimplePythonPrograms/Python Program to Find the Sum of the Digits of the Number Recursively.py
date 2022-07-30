
def sum_digits(b):
    if(b==0):
        return 0
    dig=b%10
    return dig + sum_digits(b//10)
n=int(input("Enter a number: "))
print(sum_digits(n))