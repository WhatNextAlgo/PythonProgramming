def collatz(n):
    while n > 1:
        print(n,end = " ")

        if n%2 == 0:
            n  = n// 2
        else:
            n = 3 *n + 1

    print(1,end ='')


n = int(input('Enter n: '))
print('Sequence: ', end='')
collatz(n)