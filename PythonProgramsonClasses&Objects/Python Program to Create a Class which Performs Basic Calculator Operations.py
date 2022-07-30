class Calulator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b


    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a  - self.b

    def div(self):
        return self.a/self.b

    
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

obj = Calulator(a,b)
choice = 1
while choice != 0:
    print("0. Exist")
    print("1. add")
    print("2. subtract")
    print("3. mul")
    print("4. Divide")

    choice = int(input("Enter Choice: "))
    if choice == 1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")