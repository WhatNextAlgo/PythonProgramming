"""

Series:
sin(x) = [sum (k=0..inf)] (-1)k x2k+1 / (2k+1)!
= x - (1/3!)x3 + (1/5!)x5 - (1/7!)x7
(This can be derived from Taylor's Theorem.)

cos(x) = [sum (k=0..inf)] (-1)k x2k / (2k)!
= 1 - (1/2!)x2 + (1/4!)x4 - (1/6!)x6
(This can be derived from Taylor's Theorem.)

Product:
sin(x) = x[product (k=1..inf)] (1 - (x / kPI)2)
= x(1 - (x/PI)2)(1 - (x/2PI)2)(1 - (x/3PI)2)*...


"""

import math
def cosine(x,n):
    cosx = 1
    sign = -1
    for i in range(2, n, 2):
        pi=22/7
        y=x*(pi/180)
        cosx = cosx + (sign*(y**i))/math.factorial(i)
        sign = -sign
    return cosx
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
print(round(cosine(x,n),2))