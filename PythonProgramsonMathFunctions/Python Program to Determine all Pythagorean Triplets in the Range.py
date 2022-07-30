print("""

   a = m2 - n2
       b = 2 * m * n
       c  = m2 + n2
because,
       a2 = m4 + n4 – 2 * m2 * n2
       b2 = 4 * m2 * n2
       c2 = m4 + n4 + 2* m2 * n2
""")
limits = int(input("Enter Number: "))

# c = 0
# m = 2
# while c < limits:
#     for n in range(1,m):
#         a = m*m - n*n
#         b = 2 * m * n
#         c = m*m + n * n

#         if c > limits:
#             break
#         if(a==0 or b==0 or c==0):
#             break

#         print(a,b,c)
#     m = m +1
    
import math
def pythagorean_triplet(n):
  for b in range(n):
    for a in range(1, b):
        c = math.sqrt( a * a + b * b)
        #print(c, "outer side")
        if c % 1 == 0:
            #print(c, "inner side")
            print(a, b, int(c))
            
pythagorean_triplet(limits)
