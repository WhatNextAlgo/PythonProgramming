b = input("Enter Number: ")


def binary_to_gray(n):
    n = int(n,2)
    n ^= (n >> 1)

    return bin(n)[2:]


print(binary_to_gray(b))
