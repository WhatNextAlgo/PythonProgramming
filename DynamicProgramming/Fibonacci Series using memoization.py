def fibonacci(n,memo):
    if n == 1:
        return 0
    if n == 2:
        return 1

    if not n in memo:
        memo[n] = fibonacci(n - 1,memo) + fibonacci(n - 2,memo)
    return memo[n]


myDict = {}

print(fibonacci(7,myDict))

