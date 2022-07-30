def last(n):
    return n[-1]

def sort(tuples):
    return sorted(tuples, key=last)

a=input("Enter a list of tuples:")
print("Sorted:")
print(sort(eval(a)))