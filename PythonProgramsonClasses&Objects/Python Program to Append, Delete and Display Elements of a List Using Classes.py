class AList:
    def __init__(self):
        self.alist = []


    def append(self,a):
        self.alist.append(a)

    def remove(self,a):
        self.alist.remove(a)

    def display(self):
        return self.alist



obj = AList()

choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")

    choice = int(input("Enter Choice: "))
    if choice ==1:
        n = int(input("Enter number to append: "))
        obj.append(n)
        print("List : ",obj.display())

    elif choice == 2:
        n = int(input("Enter number to delete: "))
        obj.remove(n)
        print("List : ",obj.display())

    elif choice ==3:
        print("List : ",obj.display())
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid Choice!!")

print()
