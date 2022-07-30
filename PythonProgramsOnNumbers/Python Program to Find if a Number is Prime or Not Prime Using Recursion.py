
def check(n, div = None):
    if div is None:
        div  = n// 2 + 1

    while div >= 2:
        if n % div == 0:
            print(f"{n} is not a prime number")
            return False
        else:
            return check(n, div -1)

    else:
        print(f"{n} is prime number")
        return True
        

n = int(input("Enter Number : "))
check(n)


