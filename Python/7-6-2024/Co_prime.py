"""
import math
n=int(input())
m=int(input())  
print(math.gcd(n,m)==1)
"""
a=int(input())
b=int(input())
for i in range(2,(min(a,b)//2)+1):
    if(a%i==0 and b%i==0):
        print("not coprime")
        break
else:
    print("Coprime")