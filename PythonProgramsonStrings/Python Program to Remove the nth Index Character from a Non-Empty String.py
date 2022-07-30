

n=int(input("Enter the index of the character to remove:"))
s=input("Enter the sring:")
def remove_nth_index(s,n):
    first_str = s[:n]
    second_str = s[n + 1:]

    return first_str + second_str

print("Modified string:")
print(remove_nth_index(s, n))