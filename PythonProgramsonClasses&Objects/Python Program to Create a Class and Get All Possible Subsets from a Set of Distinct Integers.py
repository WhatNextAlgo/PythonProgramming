class sub:
    def f1(self,s1):
        print(sorted(s1))
        return self.f2([],sorted(s1))

    def f2(self, curr, s1):  
        if s1:  
            result =  self.f2(curr + [s1[0]], s1[1:])  + self.f2(curr, s1[1:]) 
            print("Curr",curr, "0 ",[s1[0]]," 1: ", s1[1:])
            print("Result: ",result)
            return result

        print("[curr] : ",[curr])
        return [curr]  


a=[]
n=int(input("Enter number of elements of list: "))
for i in range(0,n):
    b=int(input("Enter element: "))
    a.append(b)
print("Subsets: ")
print(sub().f1(a))