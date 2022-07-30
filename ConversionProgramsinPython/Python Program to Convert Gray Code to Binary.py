g = input("Enter Number Gray Code: ")

def gray_to_binary(n):
    n = int(n,2)
    print(n)

    mask  = n
    while mask != 0:
        mask >>= 1
        print(mask)
        n ^= mask

    return bin(n)[2:]

print(gray_to_binary(g))


