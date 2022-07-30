from os import access


def number_to_binary(n):
    if n == 0:
        return []
    
    dig = n % 2
    return  number_to_binary(n // 2) + [dig]


print(number_to_binary(20))