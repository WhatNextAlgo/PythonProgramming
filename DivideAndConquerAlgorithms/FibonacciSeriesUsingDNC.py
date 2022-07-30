def fibonacci(n):
    if n == 1:
        return n
    if n == 0:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5))